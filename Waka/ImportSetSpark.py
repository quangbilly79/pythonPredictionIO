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
def importSetProperitiesEvent():
    sqlquery = """
    select c.content_id, collect_set(cast(au.author_id as string)) as author_id, collect_set(cast(ca.category_id as string)) as category_id, collect_set(cast(ta.tag_id as string)) as tag_id, collect_set(cast(se.contentset_id as string)) as contentset_id
    from waka.content_dim as c join waka.content_author_brid as au on c.content_id = au.content_id
    join waka.content_category_brid as ca on c.content_id = ca.content_id
    join waka.content_tag_brid as ta on c.content_id = ta.content_id
    join waka.contentset_content_brid as se on c.content_id = se.content_id
    group by c.content_id
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
    importSetProperitiesEvent()
    spark.stop()


#spark-submit ImportRateSpark.py --executor-memory 8G --driver-memory 8G
#localhost:7070/events.json?accessKey=lpFLJ5o83vW1B0LLGNQ7mOoZxdx43h2dUyAZpsjdkIYwwTDktM42p48gUosasnV7
# waka



