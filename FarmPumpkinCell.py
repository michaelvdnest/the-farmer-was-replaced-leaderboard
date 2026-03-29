from utils import *

def FarmPumpkinCell(dict_costs):

	if not can_farm_plant(dict_costs, Items.Pumpkin, Items.Carrot):
		return
	
	for_all(plant_pumpkin_cell)
	
	n = get_world_size()
	dict_pumpkin = {(n,n):False}
	while not can_harvest_pumpkin(dict_pumpkin):
		for_all(check_pumpkin, dict_pumpkin)
	
	harvest_pumpkin()	

def plant_pumpkin_cell(param):
	if get_entity_type() != Entities.Pumpkin:
		if can_harvest():
			harvest()
	
	if get_ground_type() == Grounds.Grassland:
		till()
		
	if get_water() < 0.5 and num_items(Items.Water) > 0:
		use_item(Items.Water)

	plant(Entities.Pumpkin)
	UseFertilizer()
					
			
def check_pumpkin(dict_pumpkin):
	can_harvest_pumpkin = get_entity_type() == Entities.Pumpkin and can_harvest()
	if not can_harvest_pumpkin:
		plant_pumpkin_cell(None)
		loc = (get_pos_x(), get_pos_y())
		dict_pumpkin[loc] = False

def can_harvest_pumpkin(dict_pumpkin):
	for item in dict_pumpkin:
		if not dict_pumpkin[item]:
			return False
	return True
	
		
def harvest_pumpkin():
	if can_harvest():
		num_item = num_items(Items.Pumpkin)
		harvest()
		num_item = num_items(Items.Pumpkin) - num_item
		print(num_item)
		clear()
		