from filter import *
import api
from classes import Obj


api.keywords.url="http://192.168.43.230:6002"




player=api.player_GET()



enemies=get_enemies()

players=sort_enemies(player,enemies)

stuff = api.objects_GET()
shotguns = sort_and_filter_p(stuff,is_shotgun,player)



while True:
    pass
