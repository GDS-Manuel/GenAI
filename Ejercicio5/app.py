from azure.data.tables import TableServiceClient
from datetime import datetime
from config import Config

my_entity = {
    u'PartitionKey': "Manuel",
    u'RowKey': "Manuel",
    u'nombre': b'Manuel'
}

table_service_client = TableServiceClient.from_connection_string(conn_str=Config.AZURE_STORAGE_KEY)
table_client = table_service_client.get_table_client(table_name=Config.AZURE_STORAGE_USER_TABLE)

entity = table_client.create_entity(entity=my_entity)