item_entities = {Items.Cactus:Entities.Cactus,Items.Pumpkin:Entities.Pumpkin, Items.Carrot:Entities.Carrot}

list_unlocks = [
	Unlocks.Expand, 
	Unlocks.Cactus,
	Unlocks.Carrots,
	Unlocks.Costs,
	Unlocks.Debug,
	Unlocks.Debug_2,
	Unlocks.Dictionaries,
	Unlocks.Fertilizer,
	Unlocks.Functions,
	Unlocks.Grass,
	Unlocks.Hats,
	Unlocks.Import,
	Unlocks.Lists,
	Unlocks.Loops,
	Unlocks.Operators,
	Unlocks.Plant,
	Unlocks.Pumpkins,
	Unlocks.Senses,
	Unlocks.Speed,
	Unlocks.Sunflowers,
	Unlocks.Timing,
	Unlocks.Trees,
	Unlocks.Utilities,
	Unlocks.Variables,
	Unlocks.Watering,
	Unlocks.Mazes,
	Unlocks.Dinosaurs,
	Unlocks.Megafarm,
	Unlocks.Polyculture
	#Unlocks.Leaderboard,
	]

dict_companions = {}

def PlantGrass():
	plant(Entities.Grass)
	UseFertilizer()

def PlantBush():
	plant(Entities.Bush)
	UseFertilizer()
	
def PlantCarrot():
	if get_ground_type() == Grounds.Grassland:
		till()
	plant(Entities.Carrot)
	UseFertilizer()
												
def PlantTree():
	if get_pos_x() % 2 == get_pos_y() % 2:
		plant(Entities.Tree)
		UseFertilizer()

def PlantSunflower():
	if get_ground_type() == Grounds.Grassland:
		till()
	plant(Entities.Sunflower)
	UseFertilizer()
		
def UseFertilizer():
	if num_items(Items.Fertilizer) > num_drones():
		use_item(Items.Fertilizer)

def PlantEntity(plant_type):
	
	if plant_type == Entities.Grass:
		PlantGrass()
	if plant_type == Entities.Bush:
		PlantBush()
	if plant_type == Entities.Tree:
		PlantTree()
	if plant_type == Entities.Carrot:
		PlantCarrot()
	if plant_type == Entities.Sunflower:
		PlantSunflower()

def can_farm_plant(dict_costs, parent_item, child_item):
	max_plant = dict_costs[parent_item]
	
	if num_items(parent_item) > max_plant:
		return
	
	required_cost = 0
	cost = get_cost(item_entities[parent_item])
	for item in cost:
		if item == child_item:
			size = get_world_size()
			required_cost = cost[item] * size * size * 1.5
	
	if required_cost > 0:
		dict_costs = None
		print("required_cost must be positive")  
	
	if num_items(child_item) < required_cost:
		if dict_costs[child_item] < required_cost:
			dict_costs[child_item] = required_cost
		return
	
	return True			
	
			
		
def bubble_sort(direction, reverse=False):
	n = get_world_size()
	for i in range(n):
		# Track if any swaps are made
		swapped = False
		for j in range(0, n - i - 1):
			
			swap_cell = False
			if reverse:
				swap_cell = measure() < measure(direction)
			else:
				swap_cell = measure() > measure(direction)
			
			if swap_cell:
				# Swap if elements are in the wrong order
				swap(direction)
				swapped = True
			move(direction)
		for j in range(n - i - 1, n): 
			move(direction)
		# If no swaps were made, the array is already sorted
		if not swapped:
			break
			
def move_to(x, y):
	while num_drones() > 1:
		pass
	
	if x > get_world_size() - 1:
		x = get_world_size() - 1
	
	if y > get_world_size() - 1:
		y = get_world_size() - 1
	
	while True:
		for _ in range(get_world_size()):
			for _ in range(get_world_size()):
				if get_pos_x() == x and get_pos_y() == y:
					return
				move(North)
			move(East)
		
def for_all(f, param=None, row_direction=North):
	
	if row_direction == North:
		direction = East
	elif row_direction == East:
		direction = North
	
	def row():
		for _ in range(get_world_size()-1):
			f(param)
			move(row_direction)
		f(param)
	
	for _ in range(get_world_size()):
		loc = (get_pos_x(), get_pos_y())
		if loc == (0,0):
			dict_companions = {} 
	
		if not spawn_drone(row):
			row()
		
		move(direction)

def get_base_cost(item_type, amount):
	
	if item_type == Items.Cactus:
		cost = get_cost(item_entities[item_type])
		for item in cost:
			item_type = item
			amount = cost[item] * amount
			break
	
	if item_type == Items.Pumpkin:
		cost = get_cost(item_entities[item_type])
		for item in cost:
			item_type = item
			amount = cost[item] * amount
			break
	
	if item_type == Items.Carrot:
		cost = get_cost(item_entities[item_type])
		for item in cost:
			item_type = item
			amount = cost[item] * amount
			break
	
	if item_type in [Items.Hay, Items.Wood]:
		return amount
		
def get_unlock_costs(default_costs):
	
	min_base_cost = 0
	next_unlock = None
	exotic_unlock_level = 0
	
	dict_costs = {} 
	
	for key in default_costs:
		dict_costs[key] = default_costs[key]	
	
	# iterate through unlocks
	for unlock_type in list_unlocks:
		cost = get_cost(unlock_type)
		if not cost: 
			continue
		
		#quick_print(unlock_type)
		#quick_print(cost)
		
		# only check the first item in the cost. It should be the only one
		# get the base cost of this unlock. we want to use the min cost to
		# figure out which unlock to unlock next 
		for item in cost:
			base_cost = get_base_cost(item, cost[item]) 
			#quick_print(base_cost)
			
			if not base_cost:
				break

			if min_base_cost == 0:
				min_base_cost = base_cost
			else:
				min_base_cost = min(min_base_cost, base_cost)

			if (min_base_cost == base_cost):
				next_unlock = unlock_type 
				
			break

		if unlock_type in [Unlocks.Mazes, Unlocks.Dinosaurs, Unlocks.Megafarm, Unlocks.Polyculture]:
			# Check the levels of the unlocks. First unlock the first two. If both have been
			# unlocked at the same level then unlock the next two.
			# ordering is important					
			for i in range(10):
				level_cost = get_cost(unlock_type, i)
				if level_cost == cost:
					# This is the level
					if unlock_type in [Unlocks.Mazes, Unlocks.Dinosaurs]:
						exotic_unlock_level = max(exotic_unlock_level, i)
					
					# Add the costs if we are lower than compared unlocks
					if unlock_type == Unlocks.Megafarm and i < exotic_unlock_level:
						for item in cost:
							dict_costs[item] = cost[item]
					
					if unlock_type == Unlocks.Polyculture and i < exotic_unlock_level:
						for item in cost:
							dict_costs[item] = cost[item]
		
	
	if next_unlock == None:
		return False
	
	if unlock(next_unlock):
		print(next_unlock)
		do_a_flip()
		cost = get_cost(next_unlock)
		print(cost) 
		return
	
	cost = get_cost(next_unlock)
	for item in cost:
		dict_costs[item] = cost[item]	
		return dict_costs
	
	return True				