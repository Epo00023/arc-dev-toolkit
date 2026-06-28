import os
from circle.web3 import utils

def init_client():
    return utils.init_developer_controlled_wallets_client(
        api_key=os.getenv("CIRCLE_API_KEY"),
        entity_secret=os.getenv("CIRCLE_ENTITY_SECRET")
    )
