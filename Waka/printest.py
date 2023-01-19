import pyspark
# from pyspark.sql import *
# spark = SparkSession.builder.getOrCreate()
# for i in range(100):
#     print("abc")

dict1 = {1:2, 3:4}
print(len(dict1))

list1 = ['956', '2', '948', '25807']
list2 = [3, 5, 7, 9]

print(len(set(list1) & set(list2)))


dict2 = {50:{'Recommend': ['37064', '1365', '1080', '1278'], 'Purchase': "['20']", 'precision': 4.0},
80:{'Recommend': ['37064', '1365', '1080', '1278'], 'Purchase': "['1374']", 'precision': 2.0},
49571:{'Recommend': ['37064', '1365', '1080', '1278'], 'Purchase': "['27781']", 'precision': 3.0},
203848:{'Recommend': ['37064', '1365', '1080', '1278'], 'Purchase': "['27754']", 'precision': 5.0},
348879:{'Recommend': ['32974', '33293', '22876', '14771'], 'Purchase': "['36545']", 'precision': 5.0},
475614:{'Recommend': ['1146', '3512', '28371', '683'], 'Purchase': "['1289', '35000']", 'precision': 10.0}}
print(list(dict2.values())[0]["precision"])

print(sorted(dict2.items(), key=lambda x_y: x_y[1]["precision"], reverse=True))