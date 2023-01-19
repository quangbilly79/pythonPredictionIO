"""
Import sample data for recommendation engine
"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8') # Fix TH tieng' viet. co' dau'

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
# def importRateEvent(): #Tao. Event Rate
#     dfRate = spark.sql("select user_id, content_id from waka.waka_pd_fact_rate order by user_id")
#     listRate = dfRate.toLocalIterator() #Co' the? dung` collect(), nhung ton' memory+
#     for row in listRate:
#         client.acreate_event(
#             event="rate",
#             entity_type="user",
#             entity_id=row["user_id"],
#             target_entity_type="item",
#             target_entity_id=row["content_id"]
#         )

def importRateEvent(row): #Tao. Event Rate
    import predictionio
    client = predictionio.EventClient(
        access_key="lpFLJ5o83vW1B0LLGNQ7mOoZxdx43h2dUyAZpsjdkIYwwTDktM42p48gUosasnV7",
        url="http://localhost:7070",
        threads=5,
        qsize=500)
    client.acreate_event(
        event="rate",
        entity_type="user",
        entity_id=row["user_id"],
        target_entity_type="item",
        target_entity_id=row["content_id"]
    )
dfRate = spark.sql("select user_id, content_id from waka.waka_pd_fact_rate order by user_id")
dfRate.foreach(importRateEvent)

def importWishlistEvent():
    dfWishlist = spark.sql("select user_id, content_id from waka.waka_pd_fact_wishlist order by user_id")
    listWishlist = dfWishlist.toLocalIterator()
    for row in listWishlist:
        client.acreate_event(
            event="wishlist",
            entity_type="user",
            entity_id=row["user_id"],
            target_entity_type="item",
            target_entity_id=row["content_id"]
        )
def importReadEvent():
    dfRead = spark.sql("select user_id, content_id, duration_time from waka.waka_pd_fact_reader order by user_id")
    listRead = dfRead.toLocalIterator()
    for row in listRead:
        client.acreate_event(
            event="read",
            entity_type="user",
            entity_id=row["user_id"],
            target_entity_type="item",
            target_entity_id=row["content_id"]
        )
def importSetProperitiesEvent():
    sqlquery = """
    select c.content_id, au.author_id as author_id, ca.category_id as category_id, ta.tag_id as tag_id, se.contentset_id as contentset_id
    from waka.content_dim as c join waka.content_author_brid as au on c.content_id = au.content_id
    join waka.content_category_brid as ca on c.content_id = ca.content_id
    join waka.content_tag_brid as ta on c.content_id = ta.content_id
    join waka.contentset_content_brid as se on c.content_id = se.content_id
    """
    dfProperities = spark.sql(sqlquery)
    listProperities = dfProperities.toLocalIterator()
    for row in listProperities:
        client.acreate_event(
            event="$set",
            entity_type="item",
            entity_id=row["content_id"],
            properties={ "author": row["author_id"],
                         "category": row["category_id"],
                         "tag": row["tag_id"],
                         "contentset": row["contentset_id"]
            }
        )

if __name__ == "__main__":
    #importSetProperitiesEvent()
    importRateEvent()
    # importReadEvent()
    # importWishlistEvent()

spark.stop()
#spark-submit ImportEventSpark.py --executor-memory 8G --driver-memory 8G
#localhost:7070/events.json?accessKey=lpFLJ5o83vW1B0LLGNQ7mOoZxdx43h2dUyAZpsjdkIYwwTDktM42p48gUosasnV7
# waka



