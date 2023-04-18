# stdlib
import os

# third party
from fastapi import FastAPI

# syft absolute
from syft.client.client import API_PATH
from syft.node.routes import make_routes
from syft.node.worker import Worker

node_name = os.environ.get("NODE_NAME", "default_node_name")
worker = Worker(name=node_name, local_db=True, sqlite_path="/storage/")
router = make_routes(worker=worker)

app = FastAPI(title="Worker")
app.include_router(router, prefix=API_PATH)
