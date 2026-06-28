from circle.web3 import utils

class CircleClient:
    def __init__(self, api_key: str, entity_secret: str):
        self.client = utils.init_developer_controlled_wallets_client(
            api_key=api_key,
            entity_secret=entity_secret
        )

    def raw(self):
        return self.client
