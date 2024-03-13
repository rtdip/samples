from rtdip_sdk.pipelines.sources import SparkKafkaEventhubSource
from rtdip_sdk.pipelines.transformers import (
    FledgeOPCUAJsonToPCDMTransformer,
    BinaryToStringTransformer,
)
from rtdip_sdk.pipelines.destinations import SparkPCDMToDeltaDestination
from rtdip_sdk.pipelines.secrets import AzureKeyVaultSecrets
from rtdip_sdk.authentication.azure import DefaultAuth
from rtdip_sdk.pipelines.utilities import SparkSessionUtility


def pipeline():
    auth = DefaultAuth().authenticate()
    token = auth.get_token("2ff814a6-3304-4ab8-85cb-cd0e6f879c1d/.default").token

    DATABRICKS_WORKSPACE = "adb-xxxxxxxxxx.x.azuredatabricks.net"
    DATABRICKS_CLUSTER_ID = "xxx-yyyyyy-zzzzzzzz"
    DATABRICKS_USER_ID = (
        "your_user_id@your_domain.com"  # required for Spark Connect on Windows
    )

    AZURE_KEYVAULT = "{YOUR-KEYVAULT-NAME}"
    AZURE_KEYVAULT_SECRET = "{YOUR-SECRET-NAME}"

    spark_remote = "sc://{}:443/;token={};x-databricks-cluster-id={};user_id={}".format(
        DATABRICKS_WORKSPACE, token, DATABRICKS_CLUSTER_ID, DATABRICKS_USER_ID
    )

    EVENTHUB_CONNECTION_STRING = AzureKeyVaultSecrets(
        vault=AZURE_KEYVAULT,
        key=AZURE_KEYVAULT_SECRET,
        credential=auth,
    ).get()
    EVENTHUB_CONSUMER_GROUP = "{YOUR-CONSUMER-GROUP}"

    DESTINATION_FLOAT = "{YOUR-FLOAT-DELTA-TABLE}"
    DESTINATION_STRING = "{YOUR-STRING-DELTA-TABLE}"
    DESTINATION_INTEGER = "{YOUR-INTEGER-DELTA-TABLE}"

    spark = SparkSessionUtility(config={}, remote=spark_remote).execute()

    source_df = SparkKafkaEventhubSource(
        spark=spark,
        options={
            "startingOffsets": "earliest",
            "maxOffsetsPerTrigger": 500000,
            "failOnDataLoss": "false",
        },
        connection_string=EVENTHUB_CONNECTION_STRING,
        consumer_group=EVENTHUB_CONSUMER_GROUP,
        decode_kafka_headers_to_amqp_properties=False,
    ).read_stream()

    transform_df = BinaryToStringTransformer(
        data=source_df, source_column_name="body", target_column_name="body"
    ).transform()

    transform_df = FledgeOPCUAJsonToPCDMTransformer(
        data=transform_df, source_column_name="body"
    ).transform()

    transform_df = transform_df.withColumn(
        "EventDate", transform_df["EventTime"].cast("date")
    )

    SparkPCDMToDeltaDestination(
        spark=spark,
        data=transform_df,
        options={
            "checkpointLocation": "dbfs:/checkpoints/rtdip-fledge-pcdm-stream-pipeline"
        },
        destination_float=DESTINATION_FLOAT,
        destination_string=DESTINATION_STRING,
        destination_integer=DESTINATION_INTEGER,
        mode="append",
        trigger="30 seconds",
        merge=False,
        try_broadcast_join=False,
        remove_nanoseconds=True,
        remove_duplicates=True,
        query_wait_interval=30,
    ).write_stream()


if __name__ == "__main__":
    pipeline()
