# Latest

[Latest](../../code-reference/query/functions/time_series/latest.md) returns the latest event values.

## Prerequisites
Ensure you have installed the RTDIP SDK as specified in the [Getting Started](../../../getting-started/installation.md#installing-the-rtdip-sdk) section.

This example is using [DefaultAuth()](../../code-reference/authentication/azure.md) and [DatabricksSQLConnection()](../../code-reference/query/connectors/db-sql-connector.md) to authenticate and connect. You can find other ways to authenticate here. The alternative built in connection methods are either by [PYODBCSQLConnection()](../../code-reference/query/connectors/pyodbc-sql-connector.md), [TURBODBCSQLConnection()](../../code-reference/query/connectors/turbodbc-sql-connector.md) or [SparkConnection()](../../code-reference/query/connectors/spark-connector.md).

## Parameters
|Name|Type|Description|
|---|---|---|
|business_unit|str|Business unit|
|region|str|Region|
|asset|str|Asset|
|data_security_level|str|Level of data security|
|tag_names|list|List of tagname or tagnames ["tag_1", "tag_2"]|

## Example
```python
--8<-- "https://raw.githubusercontent.com/rtdip/samples/main/queries/Latest/latest.py"
```