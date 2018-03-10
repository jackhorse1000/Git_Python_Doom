import requests


r= requests.get("http://192.168.43.97:6001/api/players")

print(r.json())