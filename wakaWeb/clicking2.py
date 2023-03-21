from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("example").getOrCreate()

data = [("a", "one"),
        ("a", "one"),
        ("a", "two"),
        ("b", "one"),
        ("b", "two"),
        ("c", "one"),
        ("d", "three"),
        ("d", "four"),]

# Create original df
df = spark.createDataFrame(data, ["x", "y"])

# Using count with condition (when) ~ group by + having in SQL
# Note that you can't just use count(col("y") == "one") since count will skip null values
result_df = df.groupBy("x").agg(count(when(col("y") == "one", True)).alias("count_one"))

result_df.show()
# +---+---------+
# |  x|count_one|
# +---+---------+
# |  a|        2|
# |  b|        1|
# |  c|        1|
# |  d|        0|
# +---+---------+
