import requests
import json

url = "http://0.0.0.0:6002"


def world_GET():

    r= requests.get(url+"/api/world")
    result = json.loads(r.text)
    return result

def los_GET(id1, id2):
    r = requests.get(url + "/api/world/los/" + str(id1) + "/" + str(id2))
    result = json.loads(r.text)
    return result

print(los_GET(0,0))
print(world_GET())



