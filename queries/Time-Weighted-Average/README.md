# Time Weighted Average

[Time Weighted Averages](../../code-reference/query/time-weighted-average.md) provide an unbiased average when working with irregularly sampled data. The RTDIP SDK requires the following parameters to perform time weighted average queries:

Window Size Mins - (deprecated)
Time Interval Rate - The time interval rate
Time Interval Unit - The time interval unit (second, minute, day, hour)
Window Length - Adds a longer window time for the start or end of specified date to cater for edge cases
Step - Data points with step "enabled" or "disabled". The options for step are "true", "false" or "metadata" as string types. For "metadata", the query requires that the TagName has a step column configured correctly in the meta data table

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
|data_type|str|Type of the data (float, integer, double, string)|
|tag_names|list|List of tagname or tagnames ["tag_1", "tag_2"]|
|start_date|str|Start date (Either a utc date in the format YYYY-MM-DD or a utc datetime in the format YYYY-MM-DDTHH:MM:SS or specify the timezone offset in the format YYYY-MM-DDTHH:MM:SS+zz:zz)|
|end_date|str|End date (Either a utc date in the format YYYY-MM-DD or a utc datetime in the format YYYY-MM-DDTHH:MM:SS or specify the timezone offset in the format YYYY-MM-DDTHH:MM:SS+zz:zz)|
|window_size_mins|int|(deprecated) Window size in minutes. Please use time_interval_rate and time_interval_unit below instead|
|time_interval_rate|str|The time interval rate (numeric input)|
|time_interval_unit|str|The time interval unit (second, minute, day, hour)|
|window_length|int|Add longer window time in days for the start or end of specified date to cater for edge cases|
|include_bad_data|bool|Include "Bad" data points with True or remove "Bad" data points with False|
|step|str|Data points with step "enabled" or "disabled". The options for step are "true", "false" or "metadata". "metadata" will retrieve the step value from the metadata table|

## Example
```python
--8<-- "https://raw.githubusercontent.com/rtdip/samples/main/queries/Time-Weighted-Average/time_weighted_average.py"
```