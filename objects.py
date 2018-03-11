import requests
import json
import time

url = "http://0.0.0.0:6001"

def objects_GET(url):

    r= requests.get(url+"/api/world/objects")
    result = json.loads(r.text)
    return result

print(objects_GET(url))