from circle.web3 import utils, developer_controlled_wallets
from dotenv import load_dotenv
from pathlib import Path
import os
import time
import json

# Load .env correctly (IMPORTANT FIX)
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

# ===== WALLET CONFIG (ARC TESTNET) =====
SOURCE_WALLET_ADDRESS = "0xe0d036fdbe0357e69606725e719ece3e3bb19368"
SOURCE_WALLET_BLOCKCHAIN = "ARC-TESTNET"

DESTINATION_WALLET_ADDRESS = "0x56ae7946705ef0fcf382824c0884be16770777d4"
DESTINATION_WALLET_ID = "cc791061-e67e-5ed0-b422-ce4fe1b4924d"

USDC_TOKEN_ADDRESS = "0x3600000000000000000000000000000000000000"
TRANSFER_AMOUNT = "5"

# ===== CHECK ENV =====
api_key = os.getenv("CIRCLE_API_KEY")
entity_secret = os.getenv("CIRCLE_ENTITY_SECRET")

print("API KEY LOADED:", bool(api_key))
print("ENTITY SECRET LOADED:", bool(entity_secret))

# ===== INIT CLIENT =====
client = utils.init_developer_controlled_wallets_client(
    api_key=api_key,
    entity_secret=entity_secret
)

transactions_api = developer_controlled_wallets.TransactionsApi(client)
wallets_api = developer_controlled_wallets.WalletsApi(client)

try:
    # ===== CREATE TRANSFER =====
    request = developer_controlled_wallets.CreateTransferTransactionForDeveloperRequest.from_dict({
        "walletAddress": SOURCE_WALLET_ADDRESS,
        "blockchain": SOURCE_WALLET_BLOCKCHAIN,
        "destinationAddress": DESTINATION_WALLET_ADDRESS,
        "tokenAddress": USDC_TOKEN_ADDRESS,
        "amounts": [TRANSFER_AMOUNT],
        "feeLevel": "MEDIUM"
    })

    transfer_response = transactions_api.create_developer_transaction_transfer(request)

    print(json.dumps(json.loads(transfer_response.model_dump_json()), indent=2))

except developer_controlled_wallets.ApiException as e:
    print("Circle API Error:")
    print(e)
