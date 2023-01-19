import predictionio
engine_client = predictionio.EngineClient(url="http://localhost:8000")


dictItemRecommend = {}

# for itemid in range(1000, 1100):
#     returnJson = engine_client.send_query({"item": str(itemid), "num": 4})
#     returnList = returnJson["itemScores"] #[{'item': '28918', 'score': 210.49612}, {'item': '937', 'score': 146.7216}, {'item': '16526', 'score': 122.389565}, {'item': '1227', 'score': 104.98494}]
#     result = map(lambda x: x["item"], returnList) #['37064', '1365', '1080', '1278']
#     dictItemRecommend.update({str(itemid): list(result)}) #{'1000': ['37064', '1365', '1080', '1278'], '1001': ['37
# print(dictItemRecommend)

print(engine_client.send_query({"user": "99999999999", "num": 4}))
print(engine_client.send_query({"item": "99999999999", "num": 4}))

#{'itemScores': [{'item': '317', 'score': 220.19672}, {'item': '1195', 'score': 219.22351}, {'item': '1330', 'score': 213.44518}, {'item': '1316', 'score': 199.4527}]}
# ['1005', '1013', '1014', '1021', '1023', '1033', '1040', '1048',
# '1050', '1052', '1054', '1055', '1056', '1058', '1060', '1063',
# '1067', '1075', '1077', '1078', '1080', '1083', '1086', '1087',
# '1093', '1094', '1097']
#{'1023': [{'item': '28918',
# 'item': '937',
# {'item': '16526',
# , {'item': '1227', 'score': 104.98494}]}
#1014,  {'1014': [{'item': '34865', 'score': 112.100105},
# {'item': '1281', 'score': 102.143616},
# {'item': '413', 'score': 101.04428},
# {'item': '19446', 'score': 35.072823}]},