# Plot

[Plot](../../code-reference/query/functions/time_series/plot.md) enables changing the frequency of time series observations with aggregations for Average, Min, Max, First Last and Standard Deviation. This is achieved by providing the following parameters:

Sample Rate - (deprecated)
Sample Unit - (deprecated)
Time Interval Rate - The time interval rate
Time Interval Unit - The time interval unit (second, minute, day, hour)

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
|tag_names|list|List of tagname or tagnames ["tag_1", "tag_2"]|
|start_date|str|Start date (Either a date in the format YY-MM-DD or a datetime in the format YYY-MM-DDTHH:MM:SS or specify the timezone offset in the format YYYY-MM-DDTHH:MM:SS+zz:zz)|
|end_date|str|End date (Either a date in the format YY-MM-DD or a datetime in the format YYY-MM-DDTHH:MM:SS or specify the timezone offset in the format YYYY-MM-DDTHH:MM:SS+zz:zz)|
|sample_rate|int|(deprecated) Please use time_interval_rate instead. See below.|
|sample_unit|str|(deprecated) Please use time_interval_unit instead. See below.|
|time_interval_rate|str|The time interval rate (numeric input)|
|time_interval_unit|str|The time interval unit (second, minute, day, hour)|
|include_bad_data|bool|Include "Bad" data points with True or remove "Bad" data points with False|

## Example
```python
--8<-- "https://raw.githubusercontent.com/rtdip/samples/main/queries/Plot/plot.py"
```