from rtdip_sdk.authentication.azure import DefaultAuth
from rtdip_sdk.connectors import DatabricksSQLConnection
from rtdip_sdk.queries import interpolate

auth = DefaultAuth().authenticate()
token = auth.get_token("2ff814a6-3304-4ab8-85cb-cd0e6f879c1d/.default").token
connection = DatabricksSQLConnection("{server_hostname}", "{http_path}", token)

parameters = {
    "business_unit": "{business_unit}",
    "region": "{region}", 
    "asset": "{asset_name}", 
    "data_security_level": "{security_level}", 
    "data_type": "float",
    "tag_names": ["{tag_name_1}", "{tag_name_2}"],
    "start_date": "2023-01-01",
    "end_date": "2023-01-31",
    "time_interval_rate": "15",
    "time_interval_unit": "minute",
    "agg_method": "first",
    "interpolation_method": "forward_fill",
    "include_bad_data": True,
}
x = interpolate.get(connection, parameters)
print(x)
