import requests
import pymysql.cursors
import time
timestart = time.time()
connection = pymysql.connect(host='172.25.0.101',
                             user='etl',
                             password='Vega123312##',
                             database='waka',
                             cursorclass=pymysql.cursors.DictCursor)

url = 'http://127.0.0.1:8002/engine'

def averagePrecisionAtK(list1, list2):
    # Average Precision At 4
    averagePrecisionAtK = 0
    j = 1
    for i in range(4):
        if list1[i] in list2:
            averagePrecisionAtK += (1/4)*(j/(i+1))
            #print(list1[i], '-', str(j), '-', str(i+1), '-', str((1/4)*(j/(i+1))))
            j += 1
    return averagePrecisionAtK
# Tuong tu. nhu tren, nhung k quan tam den' thu' tu.
# __Recommendations__	__Precision
# [0, 0, 1]	            1
# [0, 1, 1]	            2
# [1, 1, 1]	            3
def precision(list1, list2):
    return len(list(set(list1) & set(list2)))/4



with connection:
    with connection.cursor() as cursor:
        # Read a single record

        sqlUser = """select user_id, content from userRead7"""
        cursor.execute(sqlUser)
        result = cursor.fetchall()
        list1 = result["content"].split(",")



dictAll = {}
totalPrecision = 0
totalAveragePrecision = 0

for row in result:
    # (24480, '1742, 10976, 17737')
    userId = row[0] # 24480
    print("userId done")
    readList = row[1].split(", ") # ['1742', '10976', '17737']

    request = {"entity": "user", "id": str(row[0]), "num": 4}
    response = requests.post(url, json=request)
    print("response = requests.post(url, json=request) done")
    # {'user_id': 24480, 'result': [{'item': '19082', 'score': 107.67161}, {'item': '2510
    recommendResult = response.json()
    print("response.json() done")
    listRecommendResult = recommendResult["result"]
    listRecommendResultItem = list(map(lambda x: x["item"], listRecommendResult)) # ['19082', '2510', '17148', '18999']

    precision1 = precision(listRecommendResultItem, readList)
    averagePrecision = averagePrecisionAtK(listRecommendResultItem, readList)
    totalPrecision += precision1
    totalAveragePrecision += averagePrecision

    dictAll.update({str(userId): {"recommendResult": listRecommendResultItem, "read": readList,
                    "precision": precision1, "averagePrecision": averagePrecision
                    }})

    print({str(userId): {"recommendResult": listRecommendResultItem, "read": readList,
                    "precision": precision1, "averagePrecision": averagePrecision
                    }})
    print("-----------")

MAP = totalAveragePrecision / len(dictAll) * 100
MP = totalPrecision / len(dictAll) * 100
print(len(dictAll))
print("MAP: ", MAP)
print("MP", MP)

with open('debugPredictionIO.txt', 'w+') as f:
    # Sort lai. theo precision cho de~ debug
    for key, value in sorted(dictAll.items(), key=lambda x_y: x_y[1]["precision"],reverse=True):
        f.write('%s:%s\n' % (key, value))

# Mean Average Precision and Mean Precision
with open('resultPredictionIO.txt', 'w+') as f:
    f.write("Mean Average Precision: "+ str(MAP)+"%" + "\n" + "Mean Precision: "+ str(MP)+"%")
