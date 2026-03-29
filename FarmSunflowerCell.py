from utils import *

def FarmSunflowerCell(max_power):
	if num_items(Items.Power) > max_power:
		return
		
	for_all(plant_sunflower_cell)
	move_to(0,0)
	
	for i in range(15, 6, -1):	
		for_all(farm_sunflower_cell, i)
		
	move_to(0,0)

def plant_sunflower_cell(param):
	if get_entity_type() != Entities.Sunflower:
		if can_harvest():
			harvest()
	
	if get_ground_type() == Grounds.Grassland:
		till()
	if get_water() < 0.5 and num_items(Items.Water) > 0:
		use_item(Items.Water)
	
	if get_entity_type() != Entities.Sunflower:
		plant(Entities.Sunflower)
		UseFertilizer()
	
def farm_sunflower_cell(num_petals):
	current_petals = measure()
	if get_entity_type() == Entities.Sunflower and measure() >= num_petals and can_harvest():
		harvest()
	
		
	