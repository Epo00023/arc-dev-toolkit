from circle.web3 import developer_controlled_wallets

class WalletService:
    def __init__(self, client):
        self.api = developer_controlled_wallets.WalletsApi(client)

    def get_balance(self, wallet_id: str):
        return self.api.list_wallet_balance(id=wallet_id)

    def list_wallets(self):
        return self.api.list_wallets()
