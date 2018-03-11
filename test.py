from filter import *
import api
from classes import Obj



api.keywords.url="http://0.0.0.0:6002"


player=api.player_GET()



enemies=get_enemies()

enemies=sort_enemies(player,enemies)

stuff = api.objects_GET()
shotguns = sort_and_filter_p(stuff,is_shotgun,player)


player.turnTo(enemies[0])
player.shoot(enemies[0])

print (player.ammo['Shells'])

#espace the pillar

#
# while True:
#     player.turnTo(enemies[0])
#     time.sleep(2)
#     player.shoot(enemies[0])
#     time.sleep(0.5)
