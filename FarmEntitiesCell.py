from utils import *

def FarmEntitiesCell(dict_costs):
	for_all(farm_entity_cell, dict_costs)
	move_to(0,0)
		
def farm_entity_cell(dict_costs):
	hay_count = dict_costs[Items.Hay]
	wood_count = dict_costs[Items.Wood]
	carrot_count = dict_costs[Items.Carrot]
	
	if can_harvest():
		harvest()
	
	if get_water() < 0.5 and num_items(Items.Water) > 0:
		use_item(Items.Water)
	
	loc = (get_pos_x(), get_pos_y())
	if loc in dict_companions:
		plant_type = dict_companions[loc]
		PlantEntity(plant_type)
	
	if num_items(Items.Wood) < (wood_count + (carrot_count / 2)): 
		PlantTree()
	
	elif num_items(Items.Hay) < (hay_count + (carrot_count / 2)):
		PlantGrass()
						
	elif num_items(Items.Carrot) < carrot_count:
		PlantCarrot()
	
	else:
		PlantTree()
	
	if get_entity_type() == None:
		PlantSunflower()	
	
	companion = get_companion()
	if companion != None:
		plant_type, coord = get_companion()
		dict_companions[coord] = plant_type
