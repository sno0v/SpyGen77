#!/usr/bin/env python3
import requests
print("SpyGen77 by sno0v")
ip = input("IP: ")
r = requests.get(f"http://ip-api.com/json/{ip}")
data = r.json()
print(f"IP: {data.get('query')}")
print(f"Kota: {data.get('city')}")
