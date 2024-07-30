from rtdip_sdk.authentication.azure import DefaultAuth
from rtdip_sdk.connectors import DatabricksSQLConnection
from rtdip_sdk.queries import WeatherQueryBuilder

auth = DefaultAuth().authenticate()
token = auth.get_token("2ff814a6-3304-4ab8-85cb-cd0e6f879c1d/.default").token
connection = DatabricksSQLConnection("{server_hostname}", "{http_path}", token)

data = (
    WeatherQueryBuilder()
    .connect(connection)
    .source("{tablename_or_path}")
    .raw_grid(
        start_date="{start_date}",
        end_date="{end_date}",
        forecast_run_start_date="{forecast_run_start_date}",
        forecast_run_end_date="{forecast_run_end_date}",
        min_lat="{minimum_latitude}",
        min_lon="{minimum_longitude}",
        max_lat="{maximum_latitude}",
        max_lon="{maximum_longitude}",
    )
)

print(data)
