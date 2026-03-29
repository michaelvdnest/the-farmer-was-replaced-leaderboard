clear()
set_world_size(5)
ws = get_world_size()
substance = ws * 2**(num_unlocked(Unlocks.Mazes)-1)
goal = 109863168
rr = range(ws)

def drone_search():
	
	if get_pos_y() == 1:
		change_hat(Hats.Brown_Hat)
	if get_pos_y() == 2:
		change_hat(Hats.Cactus_Hat)
	if get_pos_y() == 3:
		change_hat(Hats.Carrot_Hat)
	if get_pos_y() == 3:
		change_hat(Hats.Gold_Hat)
			
	
	while num_items(Items.Gold) < goal:
		while use_item(Items.Weird_Substance, substance):
			continue
		if get_entity_type() == Entities.Treasure:
			if not use_item(Items.Weird_Substance, substance):
				harvest()
				plant(Entities.Bush)
				use_item(Items.Weird_Substance,substance)


for i in rr:
	for j in rr:
		spawn_drone(drone_search)
			
		move(North)
	move(East)
plant(Entities.Bush)
use_item(Items.Weird_Substance,substance)