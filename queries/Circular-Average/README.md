# Circular Average

[Circular Average](../../code-reference/query/circular-average.md) - A function that receives a dataframe of raw tag data and computes the circular mean for samples in a range, returning the results.

## Prerequisites
Ensure you have installed the RTDIP SDK as specified in the [Getting Started](../../../getting-started/installation.md#installing-the-rtdip-sdk) section.

This example is using [DefaultAuth()](../../code-reference/authentication/azure.md) and [DatabricksSQLConnection()](../../code-reference/query/db-sql-connector.md) to authenticate and connect. You can find other ways to authenticate here. The alternative built in connection methods are either by [PYODBCSQLConnection()](../../code-reference/query/pyodbc-sql-connector.md), [TURBODBCSQLConnection()](../../code-reference/query/turbodbc-sql-connector.md) or [SparkConnection()](../../code-reference/query/spark-connector.md).

## Parameters
|Name|Type|Description|
|---|---|---|
|business_unit|str|Business unit of the data|
region|str|Region|
asset|str|Asset|
data_security_level|str|Level of data security|
data_type|str|Type of the data (float, integer, double, string)
tag_names|list|List of tagname or tagnames ["tag_1", "tag_2"]|
start_date|str|Start date (Either a date in the format YY-MM-DD or a datetime in the format YYY-MM-DDTHH:MM:SS or specify the timezone offset in the format YYYY-MM-DDTHH:MM:SS+zz:zz)|
end_date|str|End date (Either a date in the format YY-MM-DD or a datetime in the format YYY-MM-DDTHH:MM:SS or specify the timezone offset in the format YYYY-MM-DDTHH:MM:SS+zz:zz)|
time_interval_rate|str|The time interval rate (numeric input)|
time_interval_unit|str|The time interval unit (second, minute, day, hour)|
lower_bound|int|Lower boundary for the sample range|
upper_bound|int|Upper boundary for the sample range|
include_bad_data|bool|Include "Bad" data points with True or remove "Bad" data points with False|

## Example
```python
--8<-- "https://raw.githubusercontent.com/rtdip/samples/main/queries/Circular-Average/circular_average.py"
```