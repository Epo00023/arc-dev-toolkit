# 🚀 ARC Dev Toolkit (Circle Developer Wallets)

A developer toolkit for interacting with Circle Developer-Controlled Wallets on **ARC Testnet**.

This project demonstrates how to create wallets, transfer USDC, and check balances using the Circle Web3 SDK.

---

## 📌 Features

- Create and manage developer-controlled wallets
- Send USDC on ARC Testnet
- Track transaction status in real-time
- Check wallet balances after transfer
- Simple CLI-style Python scripts

---

## 🧱 Tech Stack

- Python 3.10+
- Circle Web3 SDK (`circle.web3`)
- dotenv
- ARC Testnet (Circle)

---

## 📁 Project Structure

---

## ⚙️ Setup

### 1. Clone repository

```bash
git clone https://github.com/Epo00023/arc-dev-toolkit.git
cd arc-dev-toolkit
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
CIRCLE_API_KEY=your_api_key_here
CIRCLE_ENTITY_SECRET=your_entity_secret_here
python send_tokens.py
python create_wallet.py
python core/balance.py
#thank you for support
