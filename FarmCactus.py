from utils import *

def FarmCactus(max_cactus):
	while num_items(Items.Cactus) < max_cactus and num_items(Items.Power) > 50:
			
		clear()
		
		for y in range(get_world_size()):
			for x in range(get_world_size()):
				
				if can_harvest():
					harvest()
				
				if get_ground_type() == Grounds.Grassland:
					till()
				
				if get_water() < 0.5 and num_items(Items.Water) > 0:
					use_item(Items.Water)
				
				plant(Entities.Cactus)
				
				move(North)
			move(East)
			
			
		for x in range(get_world_size()):
			bubble_sort(North)
			move(East)
		
		for y in range(get_world_size()):
			bubble_sort(East)
			move(North)	
	
		num_item = num_items(Items.Cactus)
		harvest()
		num_item = num_items(Items.Cactus) - num_item
		print(num_item)	