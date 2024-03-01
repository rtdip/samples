# Fledge Eventhub to Delta Pipeline using Spark Connect

This article provides a guide on how to execute a pipeline that batch reads Fledge data from an Eventhub, transforms to the Process Control Data Model and writes it to Delta via Spark Connect/Databricks Connect v2. This pipeline was tested on an M2 Macbook Pro using VS Code in a Python (3.11) environment.

## Prerequisites
This pipeline job requires the packages:

* [rtdip-sdk](../../../../getting-started/installation.md#installing-the-rtdip-sdk)


## Components
|Name|Description|
|---------------------------|----------------------|
|[SparkEventhubSource](../../../code-reference/pipelines/sources/spark/eventhub.md)|Reads data from an Eventhub.|
|[BinaryToStringTransformer](../../../code-reference/pipelines/transformers/spark/binary_to_string.md)|Transforms Spark DataFrame column to string.|
|[FledgeOPCUAJsonToPCDMTransformer](../../../code-reference/pipelines/transformers/spark/fledge_opcua_json_to_pcdm.md)|Transforms Fledge to PCDM.|
|[SparkPCDMToDeltaDestination](../../../code-reference/pipelines/destinations/spark/pcdm_to_delta.md)|Writes to Delta in the Pross Control Data Model format|


## Example
Below is an example of reading from an Eventhub, transforming and writing to Delta using Spark Connect/Databricks Connect v2.

```python
--8<-- "https://raw.githubusercontent.com/rtdip/samples/main/pipelines/deploy/Fledge-SparkConnect-Pipeline-Databricks/pipeline.py"
```