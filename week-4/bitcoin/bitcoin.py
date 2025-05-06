import sys
import requests
import json

try:
    if len(sys.argv) != 2:
        sys.exit('Missing command-line argument ')
    x = float(sys.argv[1])
    response = requests.get('https://cs50.harvard.edu/python/2022/psets/4/bitcoin/rest.coincap.io/v3/assets/bitcoin?apiKey=bf32815aedef460f591969e7df265108f0b47ac04a4463e8dd6577fc20c272c8')
    o = response.json()
    d = o['data']
    i = d['priceUsd']
    amount = x * float(i)
    print(f"${amount:,.4f}")
except (ValueError,requests.RequestException):
    sys.exit('Command-line argument is not a number ')
