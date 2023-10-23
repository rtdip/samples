# Metadata

[Metadata](../../code-reference/query/metadata.md) queries provide contextual information for time series measurements and include information such as names, descriptions and units of measure.

## Prerequisites
Ensure you have installed the RTDIP SDK as specified in the [Getting Started](../../../getting-started/installation.md#installing-the-rtdip-sdk) section.

This example is using [DefaultAuth()](../../code-reference/authentication/azure.md) and [DatabricksSQLConnection()](../../code-reference/query/db-sql-connector.md) to authenticate and connect. You can find other ways to authenticate here. The alternative built in connection methods are either by [PYODBCSQLConnection()](../../code-reference/query/pyodbc-sql-connector.md), [TURBODBCSQLConnection()](../../code-reference/query/turbodbc-sql-connector.md) or [SparkConnection()](../../code-reference/query/spark-connector.md).

## Parameters
|Name|Type|Description|
|---|---|---|
|business_unit|str|Business unit|
|region|str|Region|
|asset|str|Asset|
|data_security_level|str|Level of data security|
|tag_names|(optional, list)|Either pass a list of tagname/tagnames ["tag_1", "tag_2"] or leave the list blank [] or leave the parameter out completely|

## Example
```python
--8<-- "https://raw.githubusercontent.com/rtdip/samples/main/queries/Metadata/metadata.py"
```