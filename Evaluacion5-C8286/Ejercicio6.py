import asyncio
from concurrent.futures import ThreadPoolExecutor
import numpy as np

def calculate_moving_average(prices, window_size=20):
    if len(prices) < window_size:
        return None
    return np.mean(prices[-window_size:])

def calculate_rsi(prices, periods=14):
    if len(prices) < periods:
        return None

    gains = [max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices))]
    losses = [max(0, prices[i - 1] - prices[i]) for i in range(1, len(prices))]

    average_gain = np.mean(gains[-periods:])
    average_loss = np.mean(losses[-periods:])

    if average_loss == 0:
        return 100

    rs = average_gain / average_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

async def stream_stock_data():
    example_data = [
        {'stock': 'AAPL', 'prices': [150 + i for i in range(30)]},  # Genera 30 datos para asegurar cálculos
        {'stock': 'GOOGL', 'prices': [1200 + i*2 for i in range(30)]}  # Genera 30 datos para asegurar cálculos
    ]
    while True:
        await asyncio.sleep(1)
        with ThreadPoolExecutor(max_workers=10) as executor:
            results = list(executor.map(analyze_stock, example_data))
        print("Processed Data:", results)

def analyze_stock(data):
    moving_average = calculate_moving_average(data['prices'])
    rsi = calculate_rsi(data['prices'])
    return {'stock': data['stock'], 'moving_average': moving_average, 'RSI': rsi}

if __name__ == "__main__":
    asyncio.run(stream_stock_data())

