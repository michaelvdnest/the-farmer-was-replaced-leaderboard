from utils import *

def FarmPumpkin(max_pumpkin):
	
	while num_items(Items.Pumpkin) < max_pumpkin and num_items(Items.Carrot) > 2500:
			
		for y in range(get_world_size()):
			for x in range(get_world_size()):
				
				if get_entity_type() != Entities.Pumpkin:
					if can_harvest():
						harvest()
				
					if get_ground_type() == Grounds.Grassland:
						till()
					
					if get_water() < 0.5 and num_items(Items.Water) > 0:
						use_item(Items.Water)
	
					plant(Entities.Pumpkin)
					UseFertilizer()
						
				move(North)
			move(East)
			
		
		can_harvest_pumpkin = False
		for y in range(get_world_size()):
			for x in range(get_world_size()):
				can_harvest_pumpkin = can_harvest()
				if not can_harvest_pumpkin:
					break
				move(North)
			if not can_harvest_pumpkin:
				break
			move(East)

		if can_harvest():
			num_item = num_items(Items.Pumpkin)
			harvest()
			num_item = num_items(Items.Pumpkin) - num_item
			print(num_item)
			clear()
	