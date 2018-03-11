from filter import *
import api
from classes import Obj


api.keywords.url="http://0.0.0.0:6002"

time.sleep(1)
player=api.player_GET()
life_id=99999

def hunt():
    pass

def spawn():
    player.turn(90)
    player.moveDistance(400)


def goto_control(target):

    id=target.id
    print (id)

    while True:
        player = api.player_GET()
        target = get_object_by_id(id)

        turn = player.GetAngleTo(target)
        dist= player.distance(target)

        if abs(turn)>10:
            player.turn_frame(turn)
            continue
        if dist>50 and abs(turn)<15:
            player.move_frame()
        break





def hunt_control(target):

    id=target.id
    print (id)
    target = get_object_by_id(id)
    #break out if ammo is zero, or switch weapon, low health,
    while target.dict['health']!=0:
        player = api.player_GET()
        target = get_object_by_id(id)

        turn = player.GetAngleTo(target)
        dist= player.distance(target)

        if dist<500 and abs(turn)<10:
            player.shoot(target)

        if abs(turn)>10:
            player.turn_frame(turn)
            continue
        if dist>50 and abs(turn)<15:
            player.move_frame()
        break


while True:
    player=api.player_GET()
    if life_id!=player.id:
        life_id=player.id
        spawn()
        time.sleep(100)
        continue
    enemies = get_enemies()
    enemies = sort_enemies(player, enemies)
    stuff = api.objects_GET()
    ammo = sort_and_filter_p(stuff,is_ammo,player)



    if player.ammo['Shells']==0:
        print("need shells")
        if player.weapons['Shotgun']==True:
            print("got my shotgun though")
            ammo=sort_and_filter_p(stuff,is_ammo,player)
            goto_control(ammo[0])
        else:
            print("need a shotgun")
            shotguns = sort_and_filter_p(stuff, is_shotgun, player)
            # player.Goto(shotguns[0])
            print(player.distance(shotguns[0]))
            goto_control(shotguns[0])
    else:
        #got killing potential
        print("on the hunt")
        target=enemies[0]
        dist=player.distance(target)
        print (dist)
        hunt_control(target)


    print("end of loop")
    # loop=input("press enter to loop\n")





