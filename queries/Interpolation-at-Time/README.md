# Interpolation at Time

[Interpolation at Time](../../code-reference/query/functions/time_series/interpolation-at-time.md) - works out the linear interpolation at a specific time based on the points before and after. This is achieved by providing the following parameter:

Timestamps - A list of timestamp or timestamps

## Prerequisites
Ensure you have installed the RTDIP SDK as specified in the [Getting Started](../../../getting-started/installation.md#installing-the-rtdip-sdk) section.

This example is using [DefaultAuth()](../../code-reference/authentication/azure.md) and [DatabricksSQLConnection()](../../code-reference/query/connectors/db-sql-connector.md) to authenticate and connect. You can find other ways to authenticate here. The alternative built in connection methods are either by [PYODBCSQLConnection()](../../code-reference/query/connectors/pyodbc-sql-connector.md), [TURBODBCSQLConnection()](../../code-reference/query/connectors/turbodbc-sql-connector.md) or [SparkConnection()](../../code-reference/query/connectors/spark-connector.md).

## Parameters
|Name|Type|Description|
|---|---|---|
|business_unit|str|Business unit of the data|
|region|str|Region|
|asset|str|Asset|
|data_security_level|str|Level of data security|
|data_type|str|Type of the data (float, integer, double, string)|
|tag_names|str|List of tagname or tagnames ["tag_1", "tag_2"]|
|timestamps|list|List of timestamp or timestamps in the format YYY-MM-DDTHH:MM:SS or YYY-MM-DDTHH:MM:SS+zz:zz where %z is the timezone. (Example +00:00 is the UTC timezone)|
|window_length|int|Add longer window time in days for the start or end of specified date to cater for edge cases.|
|include_bad_data|bool|Include "Bad" data points with True or remove "Bad" data points with False|

## Example
```python
--8<-- "https://raw.githubusercontent.com/rtdip/samples/main/queries/Interpolation-at-Time/interpolation_at_time.py"
```