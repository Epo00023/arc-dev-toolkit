from core.client import init_client
from circle.web3 import developer_controlled_wallets

SOURCE = "YOUR_SOURCE_WALLET"
DEST = "YOUR_DEST_WALLET"
TOKEN = "0x3600000000000000000000000000000000000000"

def send_tokens():
    client = init_client()
    api = developer_controlled_wallets.TransactionsApi(client)

    request = {
        "walletAddress": SOURCE,
        "blockchain": "ARC-TESTNET",
        "destinationAddress": DEST,
        "tokenAddress": TOKEN,
        "amounts": ["5"],
        "feeLevel": "MEDIUM"
    }

    res = api.create_developer_transaction_transfer(
        developer_controlled_wallets.CreateTransferTransactionForDeveloperRequest.from_dict(request)
    )

    print(res)
