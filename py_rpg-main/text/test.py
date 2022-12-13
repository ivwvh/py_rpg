from hero_engine import *
from shop import *
from battle import *
from main import *

player = make_hero(hp_curr=1,money=999999, inventory=['меч','лук','зелье'])
game = True
combat(player)