
def move_to(x, y):
	cx = get_pos_x()
	cy = get_pos_y()
	
	dx = x - cx
	dy = y - cy
	
	n = get_world_size() / 2
	wx = abs(dx) > n
	wy = abs(dy) > n
	
	quick_print(str(cy) + " " + str(y) + " " + str(dy) + " " + str(wy)) 
	
	
	while x != get_pos_x():
		if ((dx > 0 and not wx) or (dx < 0 and wx)): 
			move(East)
		else:
			move(West)

	while y != get_pos_y():
		if ((dy > 0 and not wy) or (dy < 0 and wy)): 
			move(North)
		else:
			move(South)