from filter import *
import api
from classes import Obj


api.keywords.url="http://0.0.0.0:6002"

time.sleep(1)
player=api.player_GET()

def hunt():
    pass

def spawn():
    player.turn(80)
    time.sleep(1)
    player.moveDistance(400)
    time.sleep(3)
    player.turn(-90)
    time.sleep(1)
    player.moveDistance(400)
    time.sleep(3)

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





def hunt_control(target,ratio=0.75):
    player=api.player_GET()
    target=[e for e in get_enemies() if e.id==target.id][0]
    if target.dict['health']==0:
        return
    if(player.distance(target)<400):

        player.turnTo(target)
        time.sleep(1)
        player.shoot(target)
        player.shoot(target)
    else:
        player.Goto(target,ratio)
        time.sleep(1)
        hunt_control(target)

# spawn()
while True:
    player=api.player_GET()
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





