import argparse
from core.transfer import send_tokens
from core.balance import get_balance
from core.client import init_client

def main():
    parser = argparse.ArgumentParser(description="ARC Dev Toolkit CLI")

    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("balance")
    subparsers.add_parser("transfer")

    args = parser.parse_args()

    if args.command == "balance":
        print(get_balance())

    elif args.command == "transfer":
        send_tokens()

    else:
        print("Use: balance | transfer")

if __name__ == "__main__":
    main()
