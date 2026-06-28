import os
import json
from dotenv import load_dotenv
from circle.web3 import utils, developer_controlled_wallets

load_dotenv()

client = utils.init_developer_controlled_wallets_client(
    api_key=os.getenv("CIRCLE_API_KEY"),
    entity_secret=os.getenv("CIRCLE_ENTITY_SECRET")
)

wallets_api = developer_controlled_wallets.WalletsApi(client)

# Wallet Set ID رو از خروجی قبلیت بذار اینجا
WALLET_SET_ID = "a17c4c6b-b689-5352-b7c2-ebacd7d303cf"

# 1st wallet
wallet1 = wallets_api.create_wallet(
    developer_controlled_wallets.CreateWalletRequest(
        wallet_set_id=WALLET_SET_ID,
        blockchains=["ARC-TESTNET"],
        count=1,
        account_type="EOA"
    )
)

# 2nd wallet
wallet2 = wallets_api.create_wallet(
    developer_controlled_wallets.CreateWalletRequest(
        wallet_set_id=WALLET_SET_ID,
        blockchains=["ARC-TESTNET"],
        count=1,
        account_type="EOA"
    )
)

print("WALLET 1:")
print(json.dumps(wallet1.to_dict(), indent=2, default=str))

print("\nWALLET 2:")
print(json.dumps(wallet2.to_dict(), indent=2, default=str))
