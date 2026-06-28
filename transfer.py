import os
import time
from dotenv import load_dotenv
from circle.web3 import utils, developer_controlled_wallets

load_dotenv()

client = utils.init_developer_controlled_wallets_client(
    api_key=os.getenv("CIRCLE_API_KEY"),
    entity_secret=os.getenv("CIRCLE_ENTITY_SECRET")
)

transfers_api = developer_controlled_wallets.TransfersApi(client)

SOURCE = "0xd85eac221d2515e2e80d77521813dc7a2380c109"
DEST = "0x05a2A0F4B750f56F375097D8036DC6fEd12056f1"

USDC_SEPOLIA = "0x1c7D4B196Cb0C7B01d743Fbc6116a902379C7238"

transfer = transfers_api.create_transfer(
    developer_controlled_wallets.CreateTransferRequest(
        source=SOURCE,
        destination=DEST,
        token=USDC_SEPOLIA,
        amount="1",
        idempotencyKey=str(time.time())
    )
)

print("TRANSFER CREATED:")
print(transfer)
