from sys import exit

def start():
	print "You enter a dark cave."
	print "There are 3 doors. One on the left, middle, and right."
	print "Which one do you take?"
	
	choice = raw_input("> ")
	
	if choice == "left":
		wolf_room()
	elif choice == "middle":
		slime_room()
	elif choice == "right":
		dead_end_room()
	elif choice == "leave":
		print "You flee the cave like a coward."
		exit(0)
	else:
		dead("You stumble around the cave until you die.")
		
def dead(why):
	print why, "Maybe you'll have better luck in another life!"
	exit(0)
	
def wolf_room():
	print "There is a wolf in the room."
	print "He looks very hungry."
	print "He is also in front of a door."
	print "What do you want to do?"
	wolf_sleep = False
	
	while True:
		choice = raw_input("> ")
	
		if choice == "leave":
			start()
		elif choice == "feed wolf" and not wolf_sleep:
			print "The wolf is now satisfied. He goes to sleep."
			wolf_sleep = True
		elif choice == "wake wolf" and wolf_sleep:
			dead("You woke up the wolf and he ate you.")
		elif choice == "open door" and not wolf_sleep:
			dead("The wolf notices you and eats you.")
		elif choice == "open door" and wolf_sleep:
			treasure_room()
		else:
			print "I don't know what that means."
	
def slime_room():
	print "There is a very large hungry slime in front of a door."
	print "The path looks impassible."
	print "What do you do?"
	
	choice = raw_input("> ")
	
	if choice == "leave":
		start()
	elif choice == "feed slime":
		dead("The slime feasts on you.")
	elif choice == "open door":
		dead("The slime feasts on you as you approach the door.")
	else:
		slime_room()
		
def dead_end_room():
	print "This room is a dead end."
	print "What do you do?"
	
	choice = raw_input("> ")
	
	if choice == "leave":
		start()
	elif choice == "use bomb":
		print "You use a bomb to blow a hole in the wall and enter the following room."
		treasure_room()
	else:
		dead("The room traps you inside.")
		
def treasure_room():
	print "You made it to the treasure room!"
	items = ['gold bars', 'diamonds', 'rings', 'pearls']
	print "The following items are in the room:"
	for item in items:
		print "%s" % item
	print "What items would you like to take? You can only fit two in your backpack."
	
	count = 0
	gold_bars = 0
	diamonds = 0
	rings = 0
	pearls = 0
	
	while count < 3:
		choice = raw_input("> ")
		
		if choice == "gold bars" and gold_bars == 0:
			print "You take the gold bars."
			gold_bars = 1
			count += 1
		elif choice == "diamonds" and diamonds == 0:
			print "You take the diamonds."
			diamonds = 1
			count += 1
		elif choice == "rings" and rings == 0:
			print "You take the rings."
			rings = 1
			count += 1
		elif choice == "pearls" and pearls == 0:
			print "You take the pearls."
			pearls = 1
			count += 1
		elif choice == "leave" and count == 0:
			print "You leave the room without any treasure. You survived!"
			exit(0)
		elif choice == "leave" and count != 0:
			print "You leave the room with treasure. You survived!"
			exit(0)
		else:
			print "That is not a valid choice."
			print "What would you like to take?"
	
	if count == 3:
		dead("You took more than you could handle and fell over and died.")

start()