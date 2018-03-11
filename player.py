import requests
import json
import time

url = "http://0.0.0.0:6002"


def player_GET():
    r = requests.get(url + "/api/player")
    result = json.loads(r.text)
    return result


def players_GET():

    r = requests.get(url+"/api/players")
    result = json.loads(r.text)
    return result


print(player_GET())

def player_Action(type, amount ):

    data = {
    "type": type,
    "amount": amount

    }





#     data_json = json.dumps(data)
#     headers = {'content-type': 'application/json'}
#     r = requests.post(url+"/api/player/actions", data = data_json, headers=headers)
#
# for x in range(4):
#     time.sleep(3)
#     player_Action("http://0.0.0.0:6002", "turn-left", 28)