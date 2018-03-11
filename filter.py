from api import *
from math import sqrt



closest = lambda player: sqrt((player['position']['x'])**2+(player['position']['x'])**2)


def get_all_players(url=keywords.url):
    players=players_GET(url)
    return players

def get_enemies(url=keywords.url):
    player=player_GET(url)
    players=get_all_players(url)
    print (player,players)
    enemies=[p for p in players  if p['id']!=player['id']]
    return enemies

def sort_enemies(enemies,key=closest,reverse=False):
    return sorted(enemies,key=key,reverse=reverse)


enemies=get_enemies()
enemies=sort_enemies(enemies)

print (enemies)
