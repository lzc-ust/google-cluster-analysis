from pyspark.sql import SparkSession

def load_data(spark, path):
    """
    Load the cluster data CSV file into a Spark DataFrame.
    
    Args:
        spark: A SparkSession object.
        path: Path to the CSV file.
    
    Returns:
        Spark DataFrame.
    """
    df = spark.read.option("header", True).option("inferSchema", True).csv(path)
    return df
