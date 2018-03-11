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
    pass

def weapon_control(player):
    if(player.ammo['Shells']>0 and player.weapons['Shotgun']==True and player.weapon!=3):
        api.switch_weapon(3)
    elif (player.ammo['Rockets']>0 and player.weapons['Rocket Launcher']==True and player.weapon!=5):
        api.switch_weapon(5)
    elif (player.ammo['Bullets']>0 and player.weapons['Handgun']==True and player.weapon!=2):
        api.switch_weapon(2)
    elif (player.weapons['Chaingun'] == True and player.weapon != 1):
        api.switch_weapon(1)
    else:
        api.switch_weapon(0)




def kill_control(player):
    pass

def goto_control(target):

    id=target.id
    print (id)
    
    while True:
        player = api.player_GET()
        weapon_control(player)

        # if player.weapon==1:
        #     break
        try:
            target = get_object_by_id(id)
        except:
            break
        turn = player.GetAngleTo(target)
        dist= player.distance(target)

        if api.los_GET(player.id,target.id)==False:
            player.strafe_frame(-turn)
            continue
        if abs(turn)>5:
            player.turn_frame(turn)
            continue
        if dist>30 and abs(turn)<15:
            player.move_frame()
        break





def hunt_control(target):

    id=target.id
    print (id)
    target = get_object_by_id(id)
    #break out if ammo is zero, or switch weapon, low health,
    while target.dict['health']!=0:
        player = api.player_GET()
        weapon_control(player)
        if player.weapon ==1:
            break
        target = get_object_by_id(id)

        turn = player.GetAngleTo(target)
        dist= player.distance(target)

        if api.los_GET(player.id,target.id)==False:
            player.strafe_frame(-turn)
            continue
        if dist<1000 and abs(turn)<10 and api.los_GET(player.id,target.id):
            player.shoot(target)

        if abs(turn)>5:
            player.turn_frame(turn)
            continue
        if dist>50 and abs(turn)<15:
            player.move_frame()
        break





while True:

    enemies = get_enemies()
    enemies = sort_enemies(player, enemies)
    stuff = api.objects_GET()
    ammo = sort_and_filter_p(stuff,is_shotgun_ammo,player)



    player=api.player_GET()
    if life_id!=player.id:
        life_id=player.id
        spawn()
        continue

    if player.ammo['Shells']==0 or player.weapons['Shotgun']==False:
        print("need shells")
        if player.weapons['Shotgun']==True:
            print("got my shotgun though")
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





