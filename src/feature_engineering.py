from pyspark.sql.functions import col, when, regexp_extract, lit
from pyspark.sql.types import DoubleType, IntegerType

def parse_resource_field(df, field_name, new_col_name):
    """
    Extract 'cpus' value from resource-related fields stored as stringified dicts.
    """
    # 用正则表达式提取 'cpus'字段
    df = df.withColumn(
        new_col_name,
        regexp_extract(col(field_name), r"'cpus': ([0-9\.e\-]+)", 1).cast(DoubleType())
    )
    return df

def clean_and_engineer_features(df):
    """
    Clean and feature engineer the Google Cluster dataset.
    """

    # 1. 解析资源字段
    df = parse_resource_field(df, 'resource_request', 'requested_cpus')
    df = parse_resource_field(df, 'average_usage', 'used_average_cpus')
    df = parse_resource_field(df, 'maximum_usage', 'used_maximum_cpus')

    # 2. 类型转换（字符串->数值）
    to_int_fields = ['priority', 'scheduling_class', 'vertical_scaling', 'scheduler', 'failed']
    for field in to_int_fields:
        if field in df.columns:
            df = df.withColumn(field, col(field).cast(IntegerType()))

    to_double_fields = ['start_time', 'end_time', 'time', 'instance_index', 'machine_id']
    for field in to_double_fields:
        if field in df.columns:
            df = df.withColumn(field, col(field).cast(DoubleType()))

    # 3. 填补 failed列（NULL -> 0）
    if 'failed' in df.columns:
        df = df.fillna({'failed': 0})

    # 4. 特征工程
    # 资源利用率
    df = df.withColumn(
        "resource_efficiency",
        when(col("requested_cpus") > 0, col("used_average_cpus") / col("requested_cpus")).otherwise(lit(0))
    )

    # 任务排队延迟
    df = df.withColumn(
        "queueing_delay",
        when((col("start_time").isNotNull()) & (col("time").isNotNull()), (col("start_time") - col("time"))).otherwise(None)
    )

    # 任务运行时间
    df = df.withColumn(
        "run_duration",
        when((col("end_time").isNotNull()) & (col("start_time").isNotNull()), (col("end_time") - col("start_time"))).otherwise(None)
    )

    return df
