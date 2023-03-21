from pyspark.sql.functions import *
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# define the list of item names
item_list = ["asset_min", "hpc_max", "off_median"]

# create a Spark DataFrame from the input table
df = spark.createDataFrame([
    ("hpc_max", 0.25, "2023-03-01T17:20:00.000+0000"),
    ("asset_min", 0.34, "2023-03-01T17:20:00.000+0000"),
    ("off_median", 0.30, "2023-03-01T17:30:00.000+0000"),
    ("hpc_max", 0.54, "2023-03-01T17:30:00.000+0000"),
    ("asset_min", 0.32, "2023-03-01T17:35:00.000+0000"),
    ("off_median", 0.67, "2023-03-01T17:20:00.000+0000"),
    ("asset_min", 0.54, "2023-03-01T17:30:00.000+0000"),
    ("off_median", 0.32, "2023-03-01T17:35:00.000+0000"),
    ("hpc_max", 0.67, "2023-03-01T17:35:00.000+0000")
], ["item_name", "item_value", "timestamp"])

df.show()


grouped_data = df.groupBy('timestamp').agg(collect_list(struct('item_name', 'item_value')).alias('items'))
grouped_data.show()