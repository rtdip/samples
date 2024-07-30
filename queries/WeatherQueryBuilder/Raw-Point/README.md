# Latest

[Raw](../../code-reference/query/functions/weather/raw.md) returns the latest weather event values.

## Prerequisites
Ensure you have installed the RTDIP SDK as specified in the [Getting Started](../../../getting-started/installation.md#installing-the-rtdip-sdk) section.

This example is using [DefaultAuth()](../../code-reference/authentication/azure.md) and [DatabricksSQLConnection()](../../code-reference/query/connectors/db-sql-connector.md) to authenticate and connect. You can find other ways to authenticate here. The alternative built in connection methods are either by [PYODBCSQLConnection()](../../code-reference/query/connectors/pyodbc-sql-connector.md), [TURBODBCSQLConnection()](../../code-reference/query/connectors/turbodbc-sql-connector.md) or [SparkConnection()](../../code-reference/query/connectors/spark-connector.md).

## Parameters
|Name|Type|Description|
|---|---|---|
|start_date|str|Start Date|
|end_date|str|End Date|
|forecast_run_start_date|str|Forecast Run Start Date|
|forecast_run_end_date|str|Forecast Run End Date|
|lat|str|Latitude|
|lon|str|Longitude|
|limit|int|Limit number of rows returned|
|measurement_type|str|Measurement Type|


## Example
```python
--8<-- "https://raw.githubusercontent.com/rtdip/samples/main/queries/WeatherQueryBuilder/Raw-Point/raw_point.py"
```