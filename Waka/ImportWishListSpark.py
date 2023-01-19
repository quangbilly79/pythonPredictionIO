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

if __name__ == "__main__":
    importWishlistEvent()
    spark.stop()


#spark-submit ImportRateSpark.py  --executor-memory 8G --driver-memory 8G
#spark-submit ImportReadSpark.py --executor-memory 8G --driver-memory 8G
#spark-submit ImportSetSpark.py --executor-memory 8G --driver-memory 8G
#spark-submit ImportWishListSpark.py --executor-memory 8G --driver-memory 8G
#spark-submit ImportRateSpark.py ImportReadSpark.py ImportSetSpark.py ImportWishListSpark.py --executor-memory 8G --driver-memory 8G
#localhost:7070/events.json?accessKey=lpFLJ5o83vW1B0LLGNQ7mOoZxdx43h2dUyAZpsjdkIYwwTDktM42p48gUosasnV7
# waka



