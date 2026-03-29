def DigForDinosaur(max_bone):
	while num_items(Items.Bone) < max_bone and num_items(Items.Power) > 50:		
		clear()
		
		def TryMove(direction):
			if move(direction) == False:
				num_item = num_items(Items.Bone)
				change_hat(Hats.Straw_Hat)
				num_item = num_items(Items.Bone) - num_item
				print(num_item)
				clear()
				return True
			else:
				return False
						
		if (get_world_size() % 2) != 0:
			set_world_size(get_world_size() - 1)
					
		# Clear the world
		for y in range(get_world_size()):
			for x in range(get_world_size()):
				if can_harvest():
					harvest()
				if get_ground_type() == Grounds.Grassland:
					till()
				move(North)
			move(East)							
			
		change_hat(Hats.Dinosaur_Hat)
		next_x, next_y = measure()
		
		dinosaur_harvested = False
		while (not dinosaur_harvested):
				
			if get_pos_x() == 0:
				dinosaur_harvested = TryMove(North)
			elif get_pos_y() == 0:
				dinosaur_harvested = TryMove(West) 
			elif get_pos_x() == get_world_size() - 2 and get_pos_y() != get_world_size() - 1:
				dinosaur_harvested = TryMove(North)  
			elif get_pos_x() == get_world_size() - 1 and get_pos_y() != 0:
				dinosaur_harvested = TryMove(South)	
			
			
			if get_pos_x() == get_world_size() - 1:
				if get_pos_y() == 0:
					dinosaur_harvested = TryMove(West)
			elif get_pos_y() % 2 == 0:
				dinosaur_harvested = TryMove(West)
			else:
				dinosaur_harvested = TryMove(East)