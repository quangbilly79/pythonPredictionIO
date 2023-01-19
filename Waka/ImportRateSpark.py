"""
Import sample data for recommendation engine
"""



import predictionio
from pyspark.sql import *
from pyspark.sql.functions import *

client = predictionio.EventClient(
access_key="lpFLJ5o83vW1B0LLGNQ7mOoZxdx43h2dUyAZpsjdkIYwwTDktM42p48gUosasnV7",
url="http://localhost:7070",
threads=5,
qsize=500)

spark = SparkSession. \
    builder.getOrCreate()
def importRateEvent(): #Tao. Event Rate
    dfRate = spark.sql("select user_id, content_id from waka.waka_pd_fact_rate order by user_id")
    listRate = dfRate.toLocalIterator() #Co' the? dung` collect(), nhung ton' memory+
    for row in listRate:
        client.acreate_event(
            event="rate",
            entity_type="user",
            entity_id=row["user_id"],
            target_entity_type="item",
            target_entity_id=row["content_id"]
        )

# def importRateEvent(row): #Tao. Event Rate
#     import predictionio
#     client = predictionio.EventClient(
#         access_key="lpFLJ5o83vW1B0LLGNQ7mOoZxdx43h2dUyAZpsjdkIYwwTDktM42p48gUosasnV7",
#         url="http://localhost:7070",
#         threads=5,
#         qsize=500)
#     client.acreate_event(
#         event="rate",
#         entity_type="user",
#         entity_id=row["user_id"],
#         target_entity_type="item",
#         target_entity_id=row["content_id"]
#     )
# dfRate = spark.sql("select user_id, content_id from waka.waka_pd_fact_rate order by user_id")
# dfRate.foreach(importRateEvent)


if __name__ == "__main__":
    importRateEvent()
    spark.stop()



#spark-submit ImportRateSpark.py --executor-memory 8G --driver-memory 8G
#localhost:7070/events.json?accessKey=lpFLJ5o83vW1B0LLGNQ7mOoZxdx43h2dUyAZpsjdkIYwwTDktM42p48gUosasnV7
# waka



