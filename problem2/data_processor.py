from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Data Anonymization") \
    .master("local[*]") \
    .getOrCreate()

df = spark.read.csv("large_2gb_sample.csv", header=True, inferSchema=True)

def anonymize_first_name():
    return fake.first_name()

def anonymize_last_name():
    return fake.last_name()

def anonymize_address():
    return fake.address()

anonymize_first_name_udf = udf(anonymize_first_name, StringType())
anonymize_last_name_udf = udf(anonymize_last_name, StringType())
anonymize_address_udf = udf(anonymize_address, StringType())

# Load the CSV file
df = spark.read.csv("large_2gb_sample.csv", header=True, inferSchema=True)

# Anonymize the data
df_anonymized = df.withColumn("first_name", anonymize_first_name_udf()) \
                   .withColumn("last_name", anonymize_last_name_udf()) \
                   .withColumn("address", anonymize_address_udf())

# Save the anonymized data to a new CSV file
df_anonymized.write.csv("anonymized_large_sample.csv", header=True)

# Stop Spark session
spark.stop()
