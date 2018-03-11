from filter import *
import api
from classes import Obj


api.keywords.url="http://0.0.0.0:6002"

start=input("press enter to begin")
player=api.player_GET()

def hunt():
    pass

def spawn():
    player.turn(80)
    time.sleep(1)
    player.move(200)
    time.sleep(3)
    player.turn(-90)
    time.sleep(1)
    player.move(200)
    time.sleep(2)


spawn()
while True:
    player=api.player_GET()
    enemies = get_enemies()
    enemies = sort_enemies(player, enemies)
    stuff = api.objects_GET()
    ammo = sort_and_filter_p(stuff,is_ammo,player)

    if player.ammo['Shells']==0:
        print("no shells")
        if player.weapons['Shotgun']==True:
            print("got my shotgun though")
            ammo=sort_and_filter_p(stuff,is_ammo,player)
            player.Goto(ammo)
        else:
            print("need a shotgun")
            shotguns = sort_and_filter_p(stuff, is_shotgun, player)
            player.Goto(shotguns[0])
    print("end of loop")
    loop=input("press enter to loop\n")





