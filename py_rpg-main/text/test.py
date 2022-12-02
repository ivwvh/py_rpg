
from operator import truediv
from hero_engine import *
from shop import *
from battle import *
from main import *

player = make_hero()
game = True
while game:
    visit_hub(player)