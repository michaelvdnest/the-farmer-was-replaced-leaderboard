from utils import *

def FarmSunflower(max_power):
	while num_items(Items.Power) < max_power:
		max_petals = 0
		current_petals = 0
		num_plants = 0					
		for y in range(get_world_size()):
			for x in range(get_world_size()):
				
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
				
				current_petals = measure()
				if current_petals == None:
					current_petals = 0
				if current_petals > max_petals:
					max_petals = current_petals
					max_x = get_pos_x()
					max_y = get_pos_y()
				
				num_plants = num_plants + 1
				
				move(North)
			move(East)
		
		while num_plants > 10:
			for y in range(get_world_size()):
				for x in range(get_world_size()):
					if get_entity_type() == Entities.Sunflower and measure() >= max_petals:
						if can_harvest():
							harvest()
							num_plants = num_plants - 1		 	 	
					move(North)
				move(East)
			max_petals = max_petals - 1