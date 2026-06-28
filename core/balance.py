from core.client import init_client
from circle.web3 import developer_controlled_wallets

def get_balance():
    client = init_client()
    api = developer_controlled_wallets.WalletsApi(client)

    wallet_id = "YOUR_WALLET_ID"

    res = api.list_wallet_balance(id=wallet_id)
    return res
