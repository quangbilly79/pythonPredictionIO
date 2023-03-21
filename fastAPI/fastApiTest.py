from typing import Union
from fastapi import FastAPI
import logging
from pydantic import BaseModel
import predictionio
from impala.dbapi import connect
import pymysql.cursors


#---------------Logging setup---------------
logging.basicConfig(format='%(asctime)s - %(levelname)s -%(filename)s:%(funcName)s:%(lineno)d\t%(message)s',
                    level=logging.INFO)


#---------------Two PredicitonIO Engine---------------
ur_client = predictionio.EngineClient(url="http://localhost:8012")
itemSim_client = predictionio.EngineClient(url="http://localhost:8011")

# Create an fastAPI app
app = FastAPI(debug=True)

# request schema {"entity": "user", "id": "131941", "num": 4}
class request(BaseModel):

    userId: Union[int, str, None]
    itemId: Union[int, str, None]
    num: Union[int, None] = 4

#---------------Post Request---------------
@app.post("/engine")
async def recommend_result(request: request):
    # ---------------Mysql Connection Detail---------------
    connection = pymysql.connect(host='172.25.0.101',
                                 user='etl',
                                 password='Vega123312##',
                                 database='waka',
                                 cursorclass=pymysql.cursors.DictCursor)

    # # ---------------Impala Connection Detail---------------
    # conn = connect(host='172.25.48.129', port=21050, database='waka')



    # ---------------Recommend for Item---------------
    if request.userId == None and request.itemId != None:
        print("item case")
        itemId = request.itemId # Get book id

        # ---------------Get Item Category Preference from Mysql DB---------------
        with connection:
            with connection.cursor() as cursor:
                # Read a single record
                sqlUser = f"""
                    select content_id, category_list from content_category_list
                    where content_id = {itemId}"""
                cursor.execute(sqlUser)
                rowItem = cursor.fetchone()

        # ---------------Get Item Category from Impala DW---------------
        # 27 [176, 177, 33] => Book 27 has 3 Category [176, 177, 33]
        # cursorItem = conn.cursor()
        # cursorItem.execute(f"""
        # select cd.content_id, group_concat(distinct cast(category_id as string)) as category_list
        # from content_dim as cd
        # join content_category_brid as ccb
        # on cd.content_id = ccb.content_id
        # where cd.content_id = {itemid}
        # group by cd.content_id
        # """)
        # rowItem = cursorItem.fetchone()

        # If there aren't any category => just send a normal query, no category filter, to UR Engine
        if rowItem == None:
            print("no fields case")
            returnQueryUr = ur_client.send_query({"item": str(request.itemId), "num": request.num})
        else: # If item has categories => send item with category filter (bias), to UR Engine
            print("fields case")
            #listCategoryItem = rowItem[1].split(", ")
            listCategoryItem = rowItem["category_list"].split(",")
            print("listCategoryItem: ", listCategoryItem)
            returnQueryUr = ur_client.send_query({"item": str(request.itemId), "num": request.num,
                                                  "fields": [{"name": "category", "values": listCategoryItem,"bias": 1.5}]})

        # ---------------Get Recommend Result from UR Engine---------------
        #returnQueryUr = ur_client.send_query({"item": str(request.id), "num": request.num})

        listItemScoreUr = returnQueryUr["itemScores"]
        #{ "item": "40193", "score": 122.25}, { "item": "39482", "score": 130.10 },

        # ---------------Get Recommend Result from Item Similarity Engine---------------
        # returnQueryItemSim = itemSim_client.send_query({"items": [str(request.id)], "num": request.num})
        # listItemScoreItemSim = returnQueryItemSim["itemScores"]
        # { "item": "40193", "score": 1.00}, { "item": "39482", "score": 1.00 },

        # ---------------Choose the final result between 2 Engine UR and Item Sim base on Score---------------
        # If Score from Ur Engine = 0 (Default Recommend) => Take Item Smilarity Engine result
        if listItemScoreUr[0]["score"] == 0:
            returnQueryItemSim = itemSim_client.send_query({"items": [str(request.itemId)], "num": request.num})
            listItemScoreItemSim = returnQueryItemSim["itemScores"]
            if listItemScoreItemSim != []:
                print("scoreUr = 0 and scoreItem != 0")
                return {"item_id": request.itemId, "result": listItemScoreItemSim}
            else:
                return {"item_id": request.itemId, "result": listItemScoreUr}
        # If Score from Ur Engine != 0 (Default Recommend) => Take that result
        else:
            print("scoreUr != 0 or scoreItem = 0")
            return {"item_id": request.itemId, "result": listItemScoreUr}

    # ---------------Recommend for User---------------
    elif request.userId != None:
        print("user case")
        userId = request.userId  # Get user id
        #---------------Get User Category Preference from Impala DW (Too Slow)---------------
        # cursorUser = conn.cursor()
        # cursorUser.execute(f"""select user_id, group_concat(distinct cast(ccb.category_id as string)) as category_list
        #                 from waka_pd_fact_reader as wr
        #                 join content_category_brid as ccb
        #                 on wr.content_id = ccb.content_id
        #                 where user_id = {userid} and data_date_key > 20220601 and data_date_key < 20220701
        #                 group by user_id order by user_id""")
        # rowUser = cursorUser.fetchone()
        #'352', '182, 176' =>

        # # ---------------Get User Category Preference from Mysql DB---------------
        with connection:
            with connection.cursor() as cursor:
                # Read a single record
                sqlUser = f"""
                    select user_id, category_list from user_category_list
                    where user_id = {userId}"""
                cursor.execute(sqlUser)
                rowUser = cursor.fetchone()

        if request.itemId == None: # Normal Recommend
            print("user only recommend")
            # If there aren't any category-pref => just send a normal query, no category filter, to UR Engine
            if rowUser == None:
                print("no fields case")
                returnQueryUrUser = ur_client.send_query({"user": str(request.userId), "num": request.num})
            else: # If user has categories-pref => send userid with category filter (bias), to UR Engine
                #listCategoryUser = rowUser[1].split(", ")
                listCategoryUser = rowUser["category_list"].split(",")
                print("listCategoryUser: ", listCategoryUser)
                print("fields case")
                returnQueryUrUser = ur_client.send_query({"user": str(request.userId), "num": request.num, \
                                                          "fields": [{"name": "category", "values": listCategoryUser, "bias": 1.5}]})
        elif request.itemId != None: # Contextual Recommend
            itemId = request.itemId
            print("user-item contextual recommend")
            # If there aren't any category-pref => just send a normal query, no category filter, to UR Engine
            if rowUser == None:
                print("no fields case")
                returnQueryUrUser = ur_client.send_query({"user": str(request.userId), "item": str(request.itemId),
                                                          "num": request.num})
            else:  # If user has categories-pref => send userid with category filter (bias), to UR Engine
                # listCategoryUser = rowUser[1].split(", ")
                listCategoryUser = rowUser["category_list"].split(",")
                print("listCategoryUser: ", listCategoryUser)
                print("fields case")
                returnQueryUrUser = ur_client.send_query({"user": str(request.userId), "item": str(request.itemId), "num": request.num,
                            "fields": [{"name": "category", "values": listCategoryUser, "bias": 1.5}]})

        # Get the recommended result from UR Engine
        listItemScoreUrUser = returnQueryUrUser["itemScores"]
        return {"user_id": request.userId, "result": listItemScoreUrUser}



# mo? anaconda Prompt => conda activate recommender => cd C:\Users\quang\PycharmProjects\PredictionIO\fastAPI
# uvicorn fastApiTest:app --reload --host 0.0.0.0 --port 8013
# localhost:8013/engine => {"userId": "5799255", "itemId": "3819", "num": 4}
# 2 Engine ở 2 địa chỉ localhost:5000 và localhost:5001 chạy ở server datanode-03. Anh open 2 port này là được

