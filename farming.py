import movement

def use_fertilizer():
	if num_items(Items.Fertilizer) > num_drones():
		use_item(Items.Fertilizer)
		

def plant_hay():		
	if can_harvest():
		harvest()
			
	if get_water() < 0.5 and num_items(Items.Water) > 0:
		use_item(Items.Water)
	
	if (get_entity_type() != Entities.Grass):
		plant(Entities.Grass)
	use_fertilizer()

def farm_hay():
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			movemment.move_to(x, y)
			plant_hay()
	
def farm_item(item, num):
	while num_items(item) < num:
		if (item == Items.Hay):
			farm_hay()