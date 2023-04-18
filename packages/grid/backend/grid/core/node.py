# syft absolute
from syft.node.worker import Worker
from syft.node.worker import create_worker_metadata
from syft.store.mongo_client import MongoStoreClientConfig
from syft.store.mongo_document_store import MongoStoreConfig
from syft.store.sqlite_document_store import SQLiteStoreClientConfig
from syft.store.sqlite_document_store import SQLiteStoreConfig

# grid absolute
from grid.core.config import settings

mongo_client_config = MongoStoreClientConfig(
    hostname=settings.MONGO_HOST,
    port=settings.MONGO_PORT,
    username=settings.MONGO_USERNAME,
    password=settings.MONGO_PASSWORD,
)

mongo_store_config = MongoStoreConfig(client_config=mongo_client_config)


client_config = SQLiteStoreClientConfig(path="/storage/")
sql_store_config = SQLiteStoreConfig(client_config=client_config)
worker = Worker(
    action_store_config=sql_store_config, document_store_config=mongo_store_config
)
create_worker_metadata(worker)
