
from pyspark.sql import *
from pyspark.sql.functions import *
import requests

spark = SparkSession.builder.getOrCreate()


# Read data from MySQL into a PySpark DataFrame
jdbc_df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:mysql://172.25.0.101:3306/waka") \
    .option("driver", "com.mysql.jdbc.Driver") \
    .option("dbtable", "content_dim") \
    .option("user", "etl") \
    .option("password", "Vega123312##") \
    .load()

distinct_content_ids = jdbc_df.dropDuplicates(["content_id"]).filter(col("status") == "ACT")\
    .select("content_id").orderBy("content_id")
collectContent_Id = distinct_content_ids.collect()


url = 'https://rec.ovp.vn/b/queries.json'
contentScore0 = []
count = 1846
for row in collectContent_Id:
    if row["content_id"] <= 4807:
        continue
    item = row["content_id"] #int
    payload = {"item": str(item), "num": 4}
    response = requests.post(url, json=payload)
    data = response.json()
    if data["itemScores"][0]["score"] == 0.0:
        print(row["content_id"], data)
        count += 1
        print(count)
        contentScore0.append(item)
    else:
        print("score != 0 ", row["content_id"], data)

print(contentScore0)
print(len(contentScore0))
# count 617, id 1136
# count 1846, id 4807
# 5000