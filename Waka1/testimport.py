import predictionio
from pyspark.sql import *
from pyspark.sql.functions import *





spark = SparkSession. \
    builder.getOrCreate()

client = EventClient(
	access_key="u8Ecc-tm8lIJABAkn7Iqd0pIwY8M6dGflPTRdUCCotMa0XBRDD-DSfcxl-D3ov4e",
        url="http://vftsandbox-node02:7070",
        threads=5,
        qsize=500)
def importRateEvent(row): #Tao. Event Rate
    client.create_event(
        event="rate",
        entity_type="user",
        entity_id=row["user_id"],
        target_entity_type="item",
        target_entity_id=row["content_id"]
    )

dfRate = spark.sql("select user_id, content_id from waka.waka_pd_fact_rate order by user_id")
dfRate.foreach(importRateEvent)
dfRate.show()


#spark-submit --py-files=predictionio.zip --executor-memory 4G --driver-memory 4G testimport.py
