from api import *
from classes import Obj
from math import sqrt
from player import *


is_shotgun = lambda shotgun:shotgun['type']=='Shotgun'

def get_all_players(url=keywords.url):
    players=players_GET(url)
    return players

def get_enemies(url=keywords.url):
    player=player_GET(url)
    players=get_all_players(url)

    enemies=[p for p in players  if p['id']!=player['id']]

    enemies=[Obj(e) for e in enemies]
    return enemies

def sort_enemies(player,enemies,reverse=False):

    closest = lambda enemy: player.distance(enemy)

    return sorted(enemies,key=closest,reverse=reverse)

def sort_and_filter_p(list,pred,player,reverse=False):

    closest = lambda enemy: player.distance(enemy)

    ls=filter(pred,list)
    return sorted(ls,key=closest,reverse=reverse)


