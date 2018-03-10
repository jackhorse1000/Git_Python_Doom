import requests
import json




def world_GET(url):

    r= requests.get(url+"/api/world")
    result = json.loads(r.text())
    return result


print(world_GET())



