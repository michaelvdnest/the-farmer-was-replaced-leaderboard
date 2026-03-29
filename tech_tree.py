import farming

def unlock_tech(tech, level):
	start_time = get_time()
	while num_unlocked(tech) < level:
		cost = get_cost(tech)
		for item in cost:
			farming.farm_item(item, cost[item])
		unlock(tech)
	total_time = get_time() - start_time	
	quick_print(str(total_time) + " ! " + str(tech) + " " + str(level))
						