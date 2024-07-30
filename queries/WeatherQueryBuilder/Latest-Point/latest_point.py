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
    .latest_point(
        lat="{latitude}",
        lon="{longitude}",
    )
)

print(data)
