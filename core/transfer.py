from circle.web3 import developer_controlled_wallets

class TransferService:
    def __init__(self, client):
        self.api = developer_controlled_wallets.TransactionsApi(client)

    def send_usdc(self, source_wallet, destination, amount, token_address, blockchain):
        request = developer_controlled_wallets.CreateTransferTransactionForDeveloperRequest.from_dict({
            "walletAddress": source_wallet,
            "destinationAddress": destination,
            "amounts": [str(amount)],
            "tokenAddress": token_address,
            "blockchain": blockchain,
            "feeLevel": "MEDIUM"
        })

        return self.api.create_developer_transaction_transfer(request)
