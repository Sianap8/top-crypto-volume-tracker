import requests
import csv
import os
from datetime import datetime

def get_top_volume_coins():
    url = (
        "https://api.coingecko.com/api/v3/coins/markets"
        "?vs_currency=usd&order=volume_desc&per_page=20&page=1"
    )
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch data: HTTP {response.status_code}")
        return
    data = response.json()
    
    print("\n💰 Top 20 Coins by 24h Volume on CoinGecko:")
    print("=" * 60)
    
    # Create/open CSV file on Desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    csv_file = os.path.join(desktop_path, "top_volume_history.csv")
    file_exists = os.path.isfile(csv_file)
    
    with open(csv_file, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow([
                "Date", "Rank", "Name", "Symbol", "Current Price (USD)", "24h Volume (USD)"
            ])
        
        today = datetime.now().strftime("%Y-%m-%d")
        for i, coin in enumerate(data, start=1):
            name = coin.get("name", "N/A")
            symbol = coin.get("symbol", "N/A")
            price = coin.get("current_price", "N/A")
            volume = coin.get("total_volume", "N/A")
            print(f"{i}. {name} ({symbol.upper()}) - Price: ${price}, 24h Volume: ${volume:,}")
            writer.writerow([today, i, name, symbol.upper(), price, volume])

if __name__ == "__main__":
    get_top_volume_coins()
