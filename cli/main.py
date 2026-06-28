from core.client import CircleClient
from core.transfer import TransferService
from config.settings import CIRCLE_API_KEY, CIRCLE_ENTITY_SECRET

def main():
    client = CircleClient(CIRCLE_API_KEY, CIRCLE_ENTITY_SECRET).raw()
    transfer = TransferService(client)

    print("ARC CLI Ready")

    # test transfer (example only)
    result = transfer.send_usdc(
        source_wallet="YOUR_SOURCE",
        destination="YOUR_DEST",
        amount=5,
        token_address="0x3600000000000000000000000000000000000000",
        blockchain="ARC-TESTNET"
    )

    print(result)

if __name__ == "__main__":
    main()
