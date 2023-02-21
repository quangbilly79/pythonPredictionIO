from pyspark.sql import *
from pyspark.sql.functions import *
import predictionio
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests

ur_client = predictionio.EngineClient(url="http://localhost:8000")
itemSim_client = predictionio.EngineClient(url="http://localhost:8001")
url = 'http://localhost:8002/engine'
request = {"entity": "item", "id": "40826", "num": 4}

response = requests.post(url, json=request)

data = response.json()

print(data)
print(type(data))
# dictItem = {}
# dictUser = {}
# for i in range(1, 15):
#     numOfReturnRecom = 5
#     returnQueryUrUser = ur_client.send_query({"user": str(i), "num": numOfReturnRecom})
#     returnQueryUr = ur_client.send_query({"item": str(i), "num": numOfReturnRecom})
#     returnQueryItemSim = itemSim_client.send_query({"items": list(str(i)), "num": numOfReturnRecom})
#     # {'itemScores': [{'item': '24671', 'score': 9.247717}, {'item': '369
#     listUserScoreUr = returnQueryUrUser["itemScores"]
#     listItemScoreUr = returnQueryUr["itemScores"]
#     listItemScoreItemSim = returnQueryItemSim["itemScores"]
#     #[{'item': '24671', 'score': 9.247717}, {'item': '36986
#
#     print(listItemScoreUr[0]["score"])
#
#     dictItem.update({str(i) + " Ur": listItemScoreUr})
#     dictItem.update({str(i) + " ItemSim": listItemScoreItemSim})
#     dictUser.update({str(i) + " Ur": listUserScoreUr})
#
#
# with open('Item.txt', 'w+') as f:
#     for key, value in dictItem.items():
#         f.write('%s:%s\n' % (key, value))
#         f.write('\n-----------------\n')
#
# with open('User.txt', 'w+') as f:
#     for key, value in dictUser.items():
#         f.write('%s:%s\n' % (key, value))
#         f.write('\n-----------------\n')
