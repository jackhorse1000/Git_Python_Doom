from filter import *
import api
from classes import Obj



obs=api.objects_GET()
for o in obs:
    print (o.type)
start=input("press enter to begin")

api.keywords.url="http://0.0.0.0:6002"


def hunt():
    pass



def spawn():
    player.turn(80)
    time.sleep(1)
    player.move(300)



while True:
    player=api.player_GET()
    enemies = get_enemies()
    enemies = sort_enemies(player, enemies)
    stuff = api.objects_GET()
    ammo = sort_and_filter_p(stuff,is_ammo,player)

    if player.ammo['Shells']==0:
        if player.weapons['Shotgun']==True:
            ammo=sort_and_filter_p(stuff,is_ammo,player)
            player.Goto(ammo)
        else:
            shotguns = sort_and_filter_p(stuff, is_shotgun, player)
            player.Goto(shotguns[0])





