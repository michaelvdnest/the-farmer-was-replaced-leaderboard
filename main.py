from utils import *
from FarmSunflower import *
from FarmSunflowerCell import *
from FarmPumpkin import *
from FarmPumpkinCell import *
from FarmCactus import *
from FarmCactusCell import *
from DigForDinosaur import *
from TreasureHunt import *
from FarmEntities import * 
from FarmEntitiesCell import * 


default_costs = {
	Items.Power:20000,
	Items.Gold:512000,
	Items.Bone:1300000,
	Items.Pumpkin:0,
	Items.Cactus:0,
	Items.Hay:0,
	Items.Wood:0,
	Items.Carrot:0}

	
clear()

while True:
	
	dict_costs = get_unlock_costs(default_costs)
	while (dict_costs == None):
		dict_costs = get_unlock_costs(default_costs)
	
	if not dict_costs:
		dict_costs = default_costs	
	
	if get_pos_x() == 0 and get_pos_y() == 0:
		FarmSunflowerCell(dict_costs[Items.Power])
						
	if get_pos_x() == 0 and get_pos_y() == 0:
		FarmPumpkinCell(dict_costs)
	
	if get_pos_x() == 0 and get_pos_y() == 0:
		set_world_size(5)
		FarmCactus(1600000000)
		#FarmCactusCell(dict_costs)
		
	if get_pos_x() == 0 and get_pos_y() == 0:
		DigForDinosaur(dict_costs[Items.Bone])
		
	if get_pos_x() == 0 and get_pos_y() == 0:
		TreasureHunt(dict_costs[Items.Gold])
																
	if get_pos_x() == 0 and get_pos_y() == 0:
		FarmEntitiesCell(dict_costs)
		