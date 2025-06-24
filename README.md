# 🪙 Binance Futures Trading Bot (Testnet)

This is a command-line based **Binance Futures Testnet Trading Bot** written in Python. It allows you to place and manage trades (Market, Limit, Stop-Limit, and Stop-Market) via the official `python-binance` library.

> ✅ Developed as part of the hiring assignment: *Junior Python Developer – Crypto Trading Bot*

---

## ✅ Assignment Requirements Checklist

| Requirement                           | Status    |
|----------------------------------------|-----------|
| Register & activate Testnet account    | ✅         |
| Generate & use API credentials         | ✅         |
| Use testnet base URL                   | ✅         |
| Use python-binance or REST API         | ✅         |
| Code structured for reusability        | ✅         |
| Input/output handling via CLI          | ✅         |
| Log API requests, responses, errors    | ✅         |
| Place market and limit orders          | ✅         |
| Support both buy and sell              | ✅         |
| Error handling                         | ✅         |
| Output order details and status        | ✅         |
| Accept and validate user input         | ✅         |
| (Bonus) Stop-Limit order               | ✅         |
| (Bonus) OCO (placeholder)              | ✅         |

---

## 🚀 Features

- **Place Order:**  
  Supports Market, Limit, Stop-Limit, and Stop-Market orders.  
  OCO is shown as a placeholder for Spot (not supported on Futures).

- **View Account Info:**  
  Displays your Futures account details.

- **View Open Orders:**  
  Lists all open Futures orders.

- **Cancel Order:**  
  Cancel an open order by symbol and order ID.

---

## 🧠 Tech Stack

- **Python 3.7+**  
- [`python-binance`](https://github.com/sammchardy/python-binance)  
- **Binance USDT-M Futures Testnet**  

---

## 📦 Installation

1. **Clone the repo**
```bash
git clone https://github.com/your-username/binance-futures-bot.git
cd binance-futures-bot
```

2. **Create a virtual environment and activate it**
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. **Install dependencies**
```bash
pip install python-binance
```

---

## 🔐 Setup API Keys (Testnet)

1. Visit [Binance Futures Testnet](https://testnet.binancefuture.com/)  
2. Register & login  
3. Navigate to **API Key** section  
4. Generate a new API key and secret  

---

## ▶️ Usage

Run the bot:

```bash
python your_script_name.py
```

You’ll be prompted to:

- Enter your **Binance Testnet API Key & Secret**
- Select an **order type** (Market, Limit, etc.)
- Input **symbol**, **side**, **quantity**, and **price/stop** if applicable

---

### 💡 Example Interaction

```
=== Binance Futures Testnet Trading Bot ===
Enter your Binance Testnet API Key:
Enter your Binance Testnet API Secret:

Main Menu:
1. Place Order
2. View Account Info
3. View Open Orders
4. Cancel Order
5. Exit
```

---

## 📄 Logs

All API requests, responses, and errors are logged in:

```
trading_bot.log
```

This file is automatically created in the project directory.

---

## 🧱 Code Structure

- **BasicBot**  
  Handles all API interactions (order placement, info, cancel).

- **InputHandler**  
  Manages user input, validation, and order parameter collection.

- **Logging**  
  All actions and errors are logged to `trading_bot.log` for traceability.

---

## 🔐 Security

- **Never share your API secret.**
- For extra safety, restrict your API key to your IP in the Binance Testnet dashboard.

---

## ⚠️ Limitations

- **OCO orders are not supported for Binance Futures** (only Spot).
- This bot is for educational and testnet use only—**do not use with real funds**.

---

## 🧾 Example Log Output

```
2025-06-24 10:14:23,382 INFO Initialized Binance Futures Testnet Client.
2025-06-24 10:15:01,743 INFO Placing order: {'symbol': 'BTCUSDT', 'side': 'BUY', 'quantity': 0.01, 'type': 'MARKET'}
2025-06-24 10:15:02,112 INFO Order response: {'orderId': 12345678, 'status': 'FILLED', ...}
```

---

## 📤 Submission

This project is developed as part of the assignment:

**"Junior Python Developer – Crypto Trading Bot"**

📧 Submit the project files and `trading_bot.log` to:
- `saami@bajarangs.com`
- `nagasai@bajarangs.com`
- CC: `sonika@primetrade.ai`

---

## 📜 License

MIT License

---

## 👨‍💻 Author

**Yashswi Shukla**  
[GitHub](https://github.com/Yashswi-3)  
[LinkedIn](https://www.linkedin.com/in/yashswi-shukla-8384ba252)
