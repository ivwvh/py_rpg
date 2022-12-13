from hero_engine import *
from shop import *
from battle import *
from main import *

player = make_hero(name="Вася Питонов",hp_max=100,money=999999, inventory=['меч','лук','зелье'])
game = True
visit_hub(player)