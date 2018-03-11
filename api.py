import requests
import json
import time

#strings for player/action

class keywords(object):
    def __init__(self,url):
        self.url=url
        self.shoot = "shoot"
        self.forward = "forward"
        self.backward = "backward"
        self.turn_left = "turn-left"
        self.turn_right = "turn-right"
        self.use = "use"
        self.strafe_left = "strafe-left"
        self.switch_weapon = "switch-weapon"

keywords=keywords("http://0.0.0.0:6002")



def player_GET(url):
    r = requests.get(url + "/api/player")
    result = json.loads(r.text)
    return result


def players_GET(url):

    r = requests.get(url+"/api/players")
    result = json.loads(r.text)
    return result



def player_Action(type, amount,url ):

    data = {
    "type": type,
    "amount": amount
    }
    data_json = json.dumps(data)
    headers = {'content-type': "application/json"}
    r=requests.post(url+"/api/player/actions",data=data_json,headers=headers)



print(player_GET(keywords.url))
player_Action(keywords.shoot,10,keywords.url)
