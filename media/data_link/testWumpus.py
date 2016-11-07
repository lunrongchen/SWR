import updatewumpusNowWithRocks
import testFOPC
# only in both solid and nowumpus lists, 
# can we be sure the cell is safe
solid = [];
nowumpus = [];
wumpus = [];
gold = [];
visited = [];
pit = [];
gotit = False;
maybeWumpus = []

# name = updatewumpusNowWithRocks.intialize_world()

# (gold,wumpus,pits):
# case 1:
# name = updatewumpusNowWithRocks.intialize_my_world("Cell 42", "Cell 32", ["Cell 31","Cell 33","Cell 44"])
# case 2:
# name = updatewumpusNowWithRocks.intialize_my_world("Cell 44", "Cell 33", ["Cell 12","Cell 24","Cell 31"])
# case 3:
# name = updatewumpusNowWithRocks.intialize_my_world("Cell 32", "Cell 13", ["Cell 31","Cell 33","Cell 44"])
# case 4:
name = updatewumpusNowWithRocks.intialize_my_world("Cell 24", "Cell 33", ["Cell 21","Cell 23","Cell 43"])

def StartGame():
	global visited, solid
	# get the perception of the initial pos.
	world = updatewumpusNowWithRocks.get_world(name)
	initial_cell = world["location"]
	initial_orientation = world["orientation"]
	initial_perception = updatewumpusNowWithRocks.update_location(world, initial_cell, initial_orientation)
	visited.append(initial_cell)
	solid.append(initial_cell)
	smart_agent(initial_perception)
	
# DFS search by call smart_mind to step in the safe cell
def smart_agent(perception):
	global solid, nowumpus, wumpus, visited, gotit

	location = perception[5]
	adjacent = updatewumpusNowWithRocks.look_ahead(name)
	perception = smart_mind(perception, location, adjacent)
	score = perception[8]
	if score == 1100:
		print "gotit"
		gotit = True;
		return;
	for next in adjacent:
		if gotit:
			return;
		curr_location = updatewumpusNowWithRocks.get_world(name)["location"]
		if curr_location != location:
			move(location, curr_location)
		if next in visited:
			continue;
		elif next in solid:
			if len(wumpus) == 1 or (next in nowumpus):
				new_perception = move(next, location)
				visited.append(next);
				smart_agent(new_perception);
				# if return back in the same path, code here:
				# print location
				curr_location = updatewumpusNowWithRocks.get_world(name)["location"]
				move(location, curr_location)

def move(next, location):
	direction = get_direction(next, location)
	updatewumpusNowWithRocks.take_action(name, direction)
	new_perception = updatewumpusNowWithRocks.take_action(name, "Step")
	return new_perception

# (smell, air, glitter, bump, scream, location, orientation, status, score)
# analyze the perception and get the adjacent cell information
def smart_mind(perception, location, adjacent):
	global solid, nowumpus, wumpus, gold, pit, maybeWumpus

	if perception[1] == 'calm':
		statement_calm = ('Calm', location)
		for next in adjacent:
			statement_adjacent = ('Adjacent', location, next)
			if testFOPC.is_solid(statement_calm, statement_adjacent):
				if next not in solid:
					solid.append(next)

	if perception[1] == 'breeze':
		for next in adjacent:
			if next not in solid:
				if len(pit) == 3:
					if next not in pit:
						solid.append(next);
					continue;
				direction = get_direction(next, location)
				updatewumpusNowWithRocks.take_action(name, direction)
				if next not in pit:
					if 'Quiet' == updatewumpusNowWithRocks.take_action(name, "Toss"):
						pit.append(next);
						nowumpus.append(next);
					else:
						if next not in solid:
							solid.append(next);

	if perception[0] == 'clean':
		statement_clean = ('Clean', location)
		for next in adjacent:
			statement_adjacent = ('Adjacent', location, next)
			if testFOPC.is_nowumpus(statement_clean, statement_adjacent):
				nowumpus.append(next)
	
	if perception[0] == 'nasty':
		temp = [];
		if len(maybeWumpus) == 0:
			for x in adjacent:
				if x not in nowumpus:
					maybeWumpus.append(x)
		else:
			for x in adjacent:
				if x in maybeWumpus and (x not in nowumpus):
					temp.append(x)
			maybeWumpus = list(temp)
		if len(maybeWumpus) == 1:
			wumpus.append(maybeWumpus[0])
		if len(wumpus) == 1:
			direction = get_direction(wumpus[0], location)
			updatewumpusNowWithRocks.take_action(name, direction)
			perception = updatewumpusNowWithRocks.take_action(name, "Shoot")

	if perception[2] == 'glitter':
		gold.append(location)
		perception = updatewumpusNowWithRocks.take_action(name, "PickUp")
	return perception

def get_direction(next, location):
	next_x = int(next[5])
	next_y = int(next[6])
	location_x = int(location[5])
	location_y = int(location[6])
	if next_x == location_x - 1:
		return "Left"
	if next_x == location_x + 1:
		return "Right"
	if next_y == location_y - 1:
		return "Down"
	if next_y == location_y + 1:
		return "Up"

def pos_to_cell(x, y):
	return "Cell "+str(x)+str(y);

StartGame()