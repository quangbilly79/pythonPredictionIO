
import predictionio

engine_client = predictionio.EngineClient(url="http://172.25.48.219:8000")

for i in range (10000,40000):
    returnQuery = engine_client.send_query({"item": str(i), "num": 4})
    listItemScore = returnQuery["itemScores"]
    if listItemScore[0]["score"] > 0:
        print("i: %d" % i)
        print(listItemScore)
print('done')