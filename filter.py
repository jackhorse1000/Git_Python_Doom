from api import *
from classes import Obj, Player
from math import sqrt
import api



is_shotgun = lambda shotgun:shotgun.type=='Shotgun'
is_ammo = lambda ammo: ammo.type=="Shotgun shells"

def get_object_by_id(id):
    ojbects=api.objects_GET()
    return [p for p in ojbects if p.id==id][0]

def get_all_players(url=keywords.url):
    players=players_GET(url)
    return players

def get_enemies(url=keywords.url):
    player=player_GET(url)
    players=get_all_players(url)

    enemies=[p for p in players  if p.id!=player.id]
    return enemies

def sort_enemies(player,enemies,reverse=False):


    closest = lambda enemy: player.distance(enemy)

    enemies=[e for e in enemies if e.dict['health']!=0]
    return sorted(enemies,key=closest,reverse=reverse)

def sort_and_filter_p(list,pred,player,reverse=False):

    closest = lambda enemy: player.distance(enemy)

    ls=filter(pred,list)
    return sorted(ls,key=closest,reverse=reverse)


