import json
import random
import logging
import time

import requests
from fastapi import (
    FastAPI,
    Body,
    BackgroundTasks
)
from starlette.requests import Request
from config import config
from core.redis_cache import RedisCache
from core.cl_waka_dao import WakaDao
import predictionio
import pymysqlpool

app = FastAPI()
pymysqlpool.logger.setLevel('INFO')
redis_cache = RedisCache(config.REDIS_SERVICE, config.SENTINEL_CONFIGS, db=5)
pool = pymysqlpool.ConnectionPool(size=2, maxsize=3, pre_create_num=2, **config.MYSQL_SERVER)
ur_client = predictionio.EngineClient(url="http://localhost:8012")
itemSim_client = predictionio.EngineClient(url="http://localhost:8011")

logging.basicConfig(format='%(asctime)s - %(levelname)s -%(filename)s:%(funcName)s:%(lineno)d\t%(message)s', level=logging.INFO)


@app.post("/queries.json")
async def book_rec(request: Request, background_tasks: BackgroundTasks, v: dict = Body(...)):
    try:
        start_time = time.time()
        logging.info("---Start book_rec: %s", v)
        request_body = json.dumps(v)
        num = int(v.get("num", 10))  # So' lg sach' trong ds kq recomemnd tra? ve`, neu' k de` cap. gi` lay' 10 cuon'
        itemid = str(v.get("item", ""))  # Lay' itemid
        userid = str(v.get("user", ""))
        waka_dao = WakaDao(redis_cache, pool)
        rowCategories = waka_dao.get_categories_by_content_id(itemid)
        logging.info("cats by content_id: %s", rowCategories)
        v['num'] = num * 3
        if not rowCategories:
            jres_ur = ur_client.send_query(v)
        else:
            listCategoryItem = rowCategories.split(",")
            v["fields"] = [{"name": "category", "values": listCategoryItem, "bias": 1.5}]
            jres_ur = ur_client.send_query(v)
        logging.info(jres_ur)
        if jres_ur['itemScores'][0]['score'] == 0:
            itemSimQuery = {
                "items": itemid,
                "num": num * 3
            }
            jres_itemSim = itemSim_client.send_query(itemSimQuery)
            if jres_itemSim and jres_itemSim['itemScores']:
                logging.info("Change to itemSim: %s", jres_itemSim)
                jres_ur = jres_itemSim

        itemScores = random.choices(jres_ur['itemScores'], k=num)
        time_process = (time.time() - start_time) * 1000
        background_tasks.add_task(write_log, itemid, userid, request_body, request.headers.get("user-agent", ""),
                                  json.dumps(itemScores), request.client.host, time_process)
        return {"itemScores": itemScores}
    except:
        return {"itemScores": []}


async def write_log(item_id, user_id, request_body, request_headers, response_body, ip, time_process):
    waka_dao = WakaDao(redis_cache, pool)
    waka_dao.write_log(item_id, user_id, request_body, request_headers, response_body, ip, time_process)
