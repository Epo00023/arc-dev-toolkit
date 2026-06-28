import os
import json
from dotenv import load_dotenv
from circle.web3 import utils, developer_controlled_wallets

load_dotenv()

api_key = os.getenv("CIRCLE_API_KEY")
entity_secret = os.getenv("CIRCLE_ENTITY_SECRET")

print("API LOADED:", bool(api_key))
print("SECRET LOADED:", bool(entity_secret))

client = utils.init_developer_controlled_wallets_client(
    api_key=api_key,
    entity_secret=entity_secret
)

wallet_sets_api = developer_controlled_wallets.WalletSetsApi(client)
wallets_api = developer_controlled_wallets.WalletsApi(client)

wallet_set = wallet_sets_api.create_wallet_set(
    developer_controlled_wallets.CreateWalletSetRequest(
        name="clean-wallet-set"
    )
)

print("WALLET SET RESPONSE:")
print(json.dumps(wallet_set.to_dict(), indent=2, default=str))
