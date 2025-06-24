import logging
from binance.client import Client
from binance.enums import *
import sys

# --- Logging Setup ---
logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)
logger = logging.getLogger(__name__)

class InputHandler:
    def __init__(self, client):
        self.client = client

    def validate_symbol(self, symbol):
        try:
            info = self.client.futures_exchange_info()
            symbols = [s['symbol'] for s in info['symbols']]
            return symbol in symbols
        except Exception as e:
            logger.error(f"Error fetching symbol info: {e}")
            return False

    def get_positive_float(self, prompt):
        while True:
            try:
                val = float(input(prompt))
                if val > 0:
                    return val
                print("Value must be positive.")
            except ValueError:
                print("Invalid number.")

    def get_order_input(self):
        print("\nSelect order type:")
        print("1. Market")
        print("2. Limit")
        print("3. Stop-Limit")
        print("4. Stop-Market")
        print("5. OCO (SPOT, not Futures)")
        order_type_map = {
            '1': 'market',
            '2': 'limit',
            '3': 'stop_limit',
            '4': 'stop_market',
            '5': 'oco'
        }
        choice = input("Enter choice (1-5): ").strip()
        order_type = order_type_map.get(choice)
        if not order_type:
            print("Invalid choice.")
            return self.get_order_input()

        symbol = input("Enter symbol (e.g., BTCUSDT): ").strip().upper()
        if not self.validate_symbol(symbol):
            print("Invalid or unsupported symbol.")
            return self.get_order_input()
        side = input("Enter side (buy/sell): ").strip().lower()
        quantity = self.get_positive_float("Enter quantity: ")
        price = stop_price = stop_limit_price = None

        if order_type in ['limit', 'stop_limit', 'oco']:
            price = self.get_positive_float("Enter limit price: ")
        if order_type in ['stop_limit', 'stop_market', 'oco']:
            stop_price = self.get_positive_float("Enter stop price (trigger): ")
        if order_type == 'oco':
            stop_limit_price = self.get_positive_float("Enter stop-limit price: ")

        # Confirmation prompt
        print(f"\nYou are about to place a {order_type.upper()} order:")
        print(f"Symbol: {symbol}, Side: {side}, Qty: {quantity}, Price: {price}, Stop: {stop_price}, StopLimit: {stop_limit_price}")
        confirm = input("Proceed? (yes/no): ").strip().lower()
        if confirm != "yes":
            print("Order cancelled.")
            return self.get_order_input()
        return symbol, side, order_type, quantity, price, stop_price, stop_limit_price

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret, testnet=testnet)
        self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        logger.info("Initialized Binance Futures Testnet Client.")

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None, stop_limit_price=None):
        try:
            params = {
                'symbol': symbol,
                'side': SIDE_BUY if side.lower() == 'buy' else SIDE_SELL,
                'quantity': quantity
            }
            if order_type == 'market':
                params['type'] = ORDER_TYPE_MARKET
            elif order_type == 'limit':
                params['type'] = ORDER_TYPE_LIMIT
                params['price'] = price
                params['timeInForce'] = TIME_IN_FORCE_GTC
            elif order_type == 'stop_limit':
                params['type'] = 'STOP'
                params['price'] = price
                params['stopPrice'] = stop_price
                params['timeInForce'] = TIME_IN_FORCE_GTC
            elif order_type == 'stop_market':
                params['type'] = 'STOP_MARKET'
                params['stopPrice'] = stop_price
            elif order_type == 'oco':
                # OCO is only supported for spot, not futures
                print("OCO orders are not supported for Binance Futures. This is a placeholder for spot OCO orders.")
                return None
            else:
                print("Unsupported order type.")
                return None

            logger.info(f"Placing order: {params}")
            order = self.client.futures_create_order(**params)
            logger.info(f"Order response: {order}")
            return order
        except Exception as e:
            # Show Binance-specific error message if available
            msg = getattr(e, 'message', str(e))
            logger.error(f"Order failed: {msg}")
            print(f"Error placing order: {msg}")
            return None

    def show_account_info(self):
        try:
            info = self.client.futures_account()
            logger.info("Fetched account info.")
            print(info)
        except Exception as e:
            logger.error(f"Error fetching account info: {e}")
            print(f"Error: {e}")

    def show_open_orders(self):
        try:
            orders = self.client.futures_get_open_orders()
            logger.info("Fetched open orders.")
            print(orders)
        except Exception as e:
            logger.error(f"Error fetching open orders: {e}")
            print(f"Error: {e}")

    def cancel_order(self, symbol, orderId):
        try:
            result = self.client.futures_cancel_order(symbol=symbol, orderId=orderId)
            logger.info(f"Cancelled order {orderId} for {symbol}")
            print(result)
        except Exception as e:
            logger.error(f"Error cancelling order: {e}")
            print(f"Error: {e}")

def main_menu(bot, input_handler):
    while True:
        print("\nMain Menu:")
        print("1. Place Order")
        print("2. View Account Info")
        print("3. View Open Orders")
        print("4. Cancel Order")
        print("5. Exit")
        choice = input("Select an option: ").strip()
        if choice == '1':
            symbol, side, order_type, quantity, price, stop_price, stop_limit_price = input_handler.get_order_input()
            order = bot.place_order(symbol, side, order_type, quantity, price, stop_price, stop_limit_price)
            if order:
                print("Order placed successfully!")
                print(order)
            else:
                print("Order failed. Check logs for details.")
        elif choice == '2':
            bot.show_account_info()
        elif choice == '3':
            bot.show_open_orders()
        elif choice == '4':
            symbol = input("Enter symbol: ").strip().upper()
            orderId = input("Enter orderId: ").strip()
            bot.cancel_order(symbol, orderId)
        elif choice == '5':
            print("Exiting bot.")
            sys.exit(0)
        else:
            print("Invalid choice.")

def main():
    print("=== Binance Futures Testnet Trading Bot ===")
    api_key = input("Enter your Binance Testnet API Key: ").strip()
    api_secret = input("Enter your Binance Testnet API Secret: ").strip()
    bot = BasicBot(api_key, api_secret, testnet=True)
    input_handler = InputHandler(bot.client)
    main_menu(bot, input_handler)

if __name__ == "__main__":
    main()
