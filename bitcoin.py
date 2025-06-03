import requests
import sys

try:
    Price = requests.get('https://api.coincap.io/v2/assets/bitcoin')
    Price.raise_for_status()
except requests.RequestException:
      sys.exit

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    WantedAmount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

Numbers = Price.json()
RealPrice = float(Numbers['data']['priceUsd'])
amount = WantedAmount * RealPrice
print(f"${amount:,.4f}")
