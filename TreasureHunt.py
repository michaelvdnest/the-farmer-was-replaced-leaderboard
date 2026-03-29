def TreasureHunt(max_gold):
	while num_items(Items.Gold) < max_gold and num_items(Items.Power) > 25:
		clear()

		plant(Entities.Bush)
		n_substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, n_substance)
		
		
		directions = [North, East, South, West]
		index = 0
		
		treasure_not_found = True
		while treasure_not_found:
			
			if get_entity_type() == Entities.Treasure:
				num_item = num_items(Items.Gold)
				harvest()
				num_item = num_items(Items.Gold) - num_item
				print(num_item)
				clear()
				treasure_not_found = False
			else:
				if move(directions[index]):
					# turn left
					index = (index - 1) % 4
				else:
					# turn right
					index = (index + 1) % 4