from utils import *

def sort_v():
	s=1 # flag turns to 0 when full row is sorted
	while s == 1:
		s = 0
		for i in range(get_world_size() - 1):
			if measure() > measure(North):
				swap(North)
				s = 1# stays '0' if no sort occurred
			move(North)
		move(North)

def sort_h():
	s=1 # flag turns to 0 when full column is sorted
	while s == 1:
		s = 0
		for i in range(get_world_size() - 1):
			if measure() > measure(East):
				swap(East)
				s = 1# stays '0' if no sort occurred
			move(East)
		move(East)
	s=1
	move(North)

def plant_cactus_cell(param):
	if get_entity_type() != Entities.Cactus:
		if can_harvest():
			harvest()
	
		if get_ground_type() == Grounds.Grassland:
			till()
			
		if get_water() < 0.5 and num_items(Items.Water) > 0:
			use_item(Items.Water)
		
	
		plant(Entities.Cactus)
		UseFertilizer()
		
def do_sort_v():
	for i in range(get_world_size()):
		if spawn_drone(sort_v):
			move(East)
		else:
			sort_v()
			move(East)
			
	if num_drones()>3:
		print("Waiting")
	while num_drones()>1:
		pass
			
def do_sort_h():
	for i in range(get_world_size()):
		if spawn_drone(sort_h):
			move(North)
		else:
			sort_h()
			move(North)
		
	if num_drones()>3:
		print("Waiting")
	while num_drones()>1:
		pass
	

def FarmCactusCell(dict_costs):

	if not can_farm_plant(dict_costs, Items.Cactus, Items.Pumpkin):
		return
	
	for_all(plant_cactus_cell)
	move_to(0,0)
	
	for n in range(3):
		do_sort_v()
	move_to(0,0)
		
	for n in range(3):
		do_sort_h()
				
	if can_harvest():
		num_item = num_items(Items.Cactus)
		harvest()
		num_item = num_items(Items.Cactus) - num_item
		print(num_item)
		clear()	
	
