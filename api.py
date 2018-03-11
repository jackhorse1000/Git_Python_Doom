import requests
import json
import time
from classes import Obj
from player import Player

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

def world_GET(url=keywords.url):

    r= requests.get(url+"/api/world")
    result = json.loads(r.text)
    return result

def los_GET( id1, id2,url=keywords.url):
    r = requests.get(url + "/api/world/los/" + str(id1) + "/" + str(id2))
    result = json.loads(r.text)
    return result

def player_GET(url=keywords.url):
    r = requests.get(url + "/api/player")
    result = json.loads(r.text)
    return Player(result)


def players_GET(url=keywords.url):

    r = requests.get(url+"/api/players")
    result = json.loads(r.text)
    result=[Obj(r) for r in result]
    return result



def player_Action(type, amount,url=keywords.url ):

    data = {
    "type": type,
    "amount": amount
    }
    data_json = json.dumps(data)
    headers = {'content-type': "application/json"}
    r=requests.post(url+"/api/player/actions",data=data_json,headers=headers)

def objects_GET(url=keywords.url):

    r= requests.get(url+"/api/world/objects")
    result = json.loads(r.text)
    result = [Obj(r) for r in result]
    return result



