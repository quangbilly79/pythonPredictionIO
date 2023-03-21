from typing import Union
from fastapi import FastAPI
import logging
from pydantic import BaseModel
import predictionio
from impala.dbapi import connect
import pymysql.cursors

# ---------------Mysql Connection Detail---------------
connection = pymysql.connect(host='172.25.0.101',
                             user='etl',
                             password='Vega123312##',
                             database='waka',
                             cursorclass=pymysql.cursors.DictCursor)
# Create an fastAPI app
app = FastAPI(debug=True)


class request(BaseModel):
    entity: str
    id: Union[int, str]
    num: Union[int, None] = 4

# ---------------Post Request---------------
@app.post("/engine")
async def recommend_result(request: request):
    # ---------------Recommend for Item---------------
    if request.entity == "item":
        print("item case")
        itemid = request.id  # Get book id

        with connection:
            with connection.cursor() as cursor:
                # Read a single record
                sqlUser = f"""
                    select content_id, category_list from content_category_list
                    where content_id = {itemid}"""
                cursor.execute(sqlUser)
                rowItem = cursor.fetchone()

        # If there aren't any category => just send a normal query, no category filter, to UR Engine
        if rowItem == None:
            print("no fields case")
            returnQueryUr = ur_client.send_query({"item": str(request.id), "num": request.num})
        else:  # If item has categories => send item with category filter (bias), to UR Engine
            print("fields case")
            # listCategoryItem = rowItem[1].split(", ")
            listCategoryItem = rowItem["category_list"].split(",")
            print("listCategoryItem: ", listCategoryItem)
            returnQueryUr = ur_client.send_query({"item": str(request.id), "num": request.num, \
                                                  "fields": [
                                                      {"name": "category", "values": listCategoryItem, "bias": 7}]})

        # ---------------Get Recommend Result from UR Engine---------------
        # returnQueryUr = ur_client.send_query({"item": str(request.id), "num": request.num})
        listItemScoreUr = returnQueryUr["itemScores"]

        if listItemScoreUr[0]["score"] == 0:
            returnQueryItemSim = itemSim_client.send_query({"items": [str(request.id)], "num": request.num})
            listItemScoreItemSim = returnQueryItemSim["itemScores"]
            if listItemScoreItemSim != []:
                print("scoreUr = 0 and scoreItem != 0")
                return {"item_id": request.id, "result": listItemScoreItemSim}
            else:
                return {"item_id": request.id, "result": listItemScoreUr}
        # If Score from Ur Engine != 0 (Default Recommend) => Take that result
        else:
            print("scoreUr != 0 or scoreItem = 0")
            return {"item_id": request.id, "result": listItemScoreUr}


# mo? anaconda Prompt => conda active recommender => cd C:\Users\quang\PycharmProjects\PredictionIO\fastAPI
# uvicorn fastApiTest:app --reload --host 0.0.0.0 --port 8013
# localhost:8013/engine => {"entity": "item", "id": "23736", "num": 4}
# 2 Engine ở 2 địa chỉ localhost:5000 và localhost:5001 chạy ở server datanode-03. Anh open 2 port này là được

