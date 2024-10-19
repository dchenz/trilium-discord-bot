import logging

from datautil import loadRequiredEnv
from trilium_client import trilium_client

logger = logging.getLogger(__name__)


client = trilium_client.DefaultApi(
    trilium_client.ApiClient(
        configuration=trilium_client.Configuration(
            host=loadRequiredEnv("TRILIUM_URL"),
        ),
        header_name="Authorization",
        header_value=loadRequiredEnv("TRILIUM_TOKEN"),
    ),
)

logger.info(client.get_app_info())
