from rtdip_sdk.authentication.azure import DefaultAuth
from rtdip_sdk.connectors import DatabricksSQLConnection
from rtdip_sdk.queries import TimeSeriesQueryBuilder

auth = DefaultAuth().authenticate()
token = auth.get_token("2ff814a6-3304-4ab8-85cb-cd0e6f879c1d/.default").token
connection = DatabricksSQLConnection("{server_hostname}", "{http_path}", token)

data = (
    TimeSeriesQueryBuilder()
    .connect(connection)
    .source("{tablename_or_path}")
    .latest(
        tagname_filter=["{tag_name_1}", "{tag_name_2}"],
    )
)

print(data)