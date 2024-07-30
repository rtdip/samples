# SQL Query Builder

[SQL Query Builder](../../code-reference/query/sql/sql_query.md) facilitates performing sql queries on underlying tables or data.

## Prerequisites
Ensure you have installed the RTDIP SDK as specified in the [Getting Started](../../../getting-started/installation.md#installing-the-rtdip-sdk) section.

This example is using [DefaultAuth()](../../code-reference/authentication/azure.md) and [DatabricksSQLConnection()](../../code-reference/query/connectors/db-sql-connector.md) to authenticate and connect. You can find other ways to authenticate here. The alternative built in connection methods are either by [PYODBCSQLConnection()](../../code-reference/query/connectors/pyodbc-sql-connector.md), [TURBODBCSQLConnection()](../../code-reference/query/connectors/turbodbc-sql-connector.md) or [SparkConnection()](../../code-reference/query/connectors/spark-connector.md).

## Parameters
|Name|Type|Description|
|---|---|---|
|sql_query|str|SQL Query to be executed|
|limit|int|Number of rows to be returned|
|offset|int|Offset to be applied to rows returned|

## Example
```python
--8<-- "https://raw.githubusercontent.com/rtdip/samples/main/queries/SQLQueryBuilder/get.py"
```