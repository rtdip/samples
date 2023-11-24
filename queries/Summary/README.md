# Summary

[Summary](../../code-reference/query/functions/time_series/summary.md) facilitates performing a summary of statisics of time series data, typically filtered by a Tag Name or Device Name and an event time.

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
|data_type|str|Type of the data (float, integer, double, string)|
|tag_names|list|List of tagname or tagnames ["tag_1", "tag_2"]|
|start_date|str|Start date (Either a date in the format YY-MM-DD or a datetime in the format YYY-MM-DDTHH:MM:SS or specify the timezone offset in the format YYYY-MM-DDTHH:MM:SS+zz:zz)|
|end_date|str|End date (Either a date in the format YY-MM-DD or a datetime in the format YYY-MM-DDTHH:MM:SS or specify the timezone offset in the format YYYY-MM-DDTHH:MM:SS+zz:zz)|
|include_bad_data|bool|Include "Bad" data points with True or remove "Bad" data points with False|

## Example
```python
--8<-- "https://raw.githubusercontent.com/rtdip/samples/main/queries/Summary/summary.py"
```