from bitarray import bitarray
from encounters_the_obsidian_house import *

####################################################
##				  --Player--					  ##
####################################################

class player:
	
	attributes = {
		"charisma" : 0,
		"strength" : 0,
		"dexterity" : 0,
		"focus" : 0
	}
	inv = []
	location = ""
	health = 100
	mental_health = 100
	condition = {
		"arm broken" : False,
		"leg crippled" : False,
		"eye blinded" : False,
		"tongue removed" : False
	}
	
	def __init__(self,location,item):
		self.location = location
		self.inv.append(item)
	def takeItem(self, thing):
		self.inv.append(thing)
		self.location.removeItem(thing)
		itemTable[thing][1] = "player"
		if thing[0] in {'a','e','i','o','u'}:
			itemTable[thing][2] = "There is an {} on the ground.\n".format(thing)
		else:
			itemTable[thing][2] = "There is a {} on the ground.\n".format(thing)
		print("\nYou take the {}.\n".format(thing))
	def dropItem(self,thing):
		self.inv.remove(thing)
		self.location.items.append(thing)
		self.location.description += itemTable[thing][2]
		print("\nYou drop the {}.\n".format(thing))
	def printAttributes(self):
		#print("\nYour attributes are:\n")
		for i in self.attributes:
			#print("\n" + i + " = " + self.attributes[i])
			print("{} = {}\n".format(i, self.attributes[i]))
	def pickAttributes(self):
		total = 20
		pick = 0
		for i in self.attributes:
			self.attributes[i] = 0
		print ("""
		Before we delve into Obsidian House, you must
		decide what type of character you wish to be.
		Choose wisely.
		For remember, there is no Fate or Destiny,
		there is only the path you carve yourself.
		I wonder what path that may be...
		
		Charisma is your persuasion, your ability to
		shroud truth or deception. Those with high scores
		are well liked by their peers.
		
		Strength is brute force and endurance. The individual
		with much strength has intimidation and
		destruction in their back pocket.
		
		Dexterity describes those nimble and silent.
		Sneaking on creaky floors, speed, and
		one's ability for acrobatic feats are dictated by
		how dexterous they are.
		
		Focus is your wildcard. Inside yourself is
		a mysterious power that feels familiar.
		With a high focus, you can control that power and,
		perhaps, stave off the influence of others...
		""")
		for i in self.attributes:
			"""if total == 0:
				print ("\nAll points spent. Your attributes are:")
				self.printAttributes()
				while True:
					finished = input("\nWould you like to continue? (Y/N)",)
					if finished.lower() == "y":
						print("Very well...")
						return
					elif finished.lower() == "n":
						self.pickAttributes()
					else:
						print("I didn't catch that.")"""
			while True:
				pick = input("{} points remaining. How many for {}? ".format(total, i))
				if pick.isdigit() == False:
					print("You must pick a number between 0 and 20.")
					continue
				pick = int(pick)
				if pick > 20 or pick < 0:
					print ("You must pick a number between 0 and 20.")
				elif pick > total:
					print ("You don't have that many points left.")
				elif pick <= 20 and pick >= 0:
					self.attributes[i] = pick
					total -= pick
					break
			if total == 0:
				print ("\nAll points spent. Your attributes are:\n")
				self.printAttributes()
				while True:
					finished = input("Would you like to continue? (Y/N)",)
					if finished.lower() == "y":
						print("\nVery well...")
						return
					elif finished.lower() == "n":
						return self.pickAttributes()
					else:
						print("I didn't catch that.")
		if total != 0:
			print("\nYou failed to use all of your points. Try again.")
			return self.pickAttributes()
	def printLocation(self, visit):
		if visit:
			print("\n--{}--\n".format(self.location.name))
		else:
			self.location.printDescription()
	def printInv(self):
		print ("\nYour pockets contain:\n")
		for i in self.inv:
			print ("\t-",i)
			print("")
	def playerMove(self, x, table):
		temp = ["north", "south", "east", "west", "up", "down"]
		for i in temp:
			if x == i[0] or x == i:
				if i in self.location.connections:
					if self.location.connections[i] in table:
						move = self.location.connections[i]
						self.location = table[move]
						return
					else:
						print(self.location.connections[i])
						return
				else:
					print("You can't go that way!")
					return
		print ("Input error")
		return
	def playerStatus(self, updates, values):
		for i in range (0, len(updates)):
			if updates[i] == "health":
				self.health = values[i]
			elif updates[i] == "mental_health":
				self.mental_health = values[i]
			elif updates[i] in self.condition:
				self.condition[updates[i]] = values[i]
	def statCheck(self, stats, values):
		for i in range(0, len(stats)):
			if self.attributes[stats[i]] < values[i]:
				return False
		return True
	def removeItem(self, thing):
		if thing in self.inv:
			self.inv.remove(thing)

####################################################
##				    --Items--					  ##
####################################################

itemTable = {
	"strange token" : ["""\nA cold stone with a rune on it.
		""", "player",None, "token"],
	"old book" : ["""\nLeather-bound and crisp.\
		\nThe elements have had no effect on its condition.
		""", "shack", "An old book stands out on top of the desk.\n", "token"],
	"chunk of metal": ["""\nDark and cold.
		""", "shack", "Shining in the lamplight, a chunk of metal lies on the ground.\n", "weapon"],
	"obsidian dagger" : ["""\nGlass, but too dense to see through, and a handle that looks wrapped with bandages.\
	\nThe blade ends jagged and flat, suggesting a break had shortened its length.
	""", "side alley", "What appears to be a dagger is stuck between two crates.", "weapon"],
	"temp" : None
}

####################################################
##				  --Locations--				  	  ##
####################################################

class location:
	
	visited = False
	
	def __init__(self, description, items, interactions, connections, name):
		self.description = description
		self.items = items
		self.interactions = interactions
		self.connections = connections
		self.name = name
	def event_changes(self):
		pass
	def printDescription(self):
		print("\n"+"--"+self.name+"--"+"\n")
		print (self.description)
	def printInteractions(self, thing):
		if i in interactions:
			print (interactions[i])
	def openObject(self, thing):
		print("\nThere is no {} to open.\n".format(thing))
	def removeItem(self, thing):
		if thing in self.items:
			self.description = self.description.replace(itemTable[thing][2],"")
			self.items.remove(thing)
	def examine_object(self, thing):
		return False

class gameState:

	events = {
		"figment" : True,
		"shack cursed" : False,
		"drunkard" : True
	}
	bitfield = bitarray()
	def updateState(self):
		pass
	def checkState(self):
		pass

class npc:
	
	def __init__(self,description,location,health,alive):
		self.description = description
		self.location = location
		self.health = health
		self.alive = alive

class PaulLowden(npc):
	def __init__(self,
			deception = "",
			location = "",
			health = 60,
			alive = True):
		npc.__init__(self,description,location,health,alive)

class frontTavern(location):

	def __init__(self,
			description = """The air at dusk is humid on the edge of the -blank- River.\
			\nYou stand to the east of a wooden building, the river at your back.\
			\nThe gray paint is chipping, but the structure appears sturdy.\
			\nThere is a sign above the door.\
			\nTo the north is a dilapidated shack, and a dark alley stares from the south.\
			\n""",
			items = [],
			interactions = {
				"sign" : """\nBlackened wood swings above the door.\
				\nThe markings on it archaic and rough.\
				\nIt reads:\
				\n\n	The Obsidian House\
				\n\n	of Vereth & Time
				""",
				"ground" : """\nMoist from a recent rain.\
				\nYour feet sink a full inch in mud.
				""",
				"door" : """\nFlat and smooth, it feels cold like stone.
				""",
				"river" : """\nIt is dark and calm.
				"""},
			connections = {
				"north" : "shack",
				"south" : "side alley",
				"east" : "\nThe door is shut.\n"},
			name = "Front Tavern"):
		location.__init__(self,description,items,interactions,connections,name)
		
	def openObject(self, thing):
		if thing == "door" and self.connections["east"] != "tavern entryway":
			self.connections["east"] = "tavern entryway"
			self.interactions["door"] = "\nWarm light and soft music spill from the doorway.\n"
			print ("""\nYou turn the cold, silver handle until there is a satisfying click.\
			\nThe door opens smooth and silent.
			""")
			self.description += "The door to the building is open.\n"
			return
		elif thing == "door":
			print ("\nThe door is already open.\n")
			return
		else:
			print ("\nThere is no {} here to open.\n".format(thing))
			return

class northTavern(location):
	def __init__(self,
			description = """Another description here.
			""",
			items = [],
			interactions = {
				"ground" : "",
				"window" : "",
				"trap door" : ""
			},
			connections = {"west" : "shack", "east": "burned storehouse"},
			name = "North Tavern"):
		location.__init__(self, description, items, interactions, connections, name)

class sideAlley(location):

####
## Garbage will contain a dagger made of dark stone.
## If player is fast enough, they can use the dagger efficiently.
## If they are strong enough, they can use the dagger to finish an enemy
## (but not very well if they try to use it to start off as they will be slow.
## They would have to beat someone first.)
####

	daggerFound = False

	def __init__(self,
			description = """The shadows are long with the sun low to the west.\
			\nA stack of garbage leans against the wall of the building,\
			\nframed by rows of fliers in exotic colors. The air is stale and\
			\nevery subtle breeze carries an acidic taste. Around the east,\
			\nthe edge of a blackened structure can be seen, while the front\
			\nof the building is back to the west.\
			\nStepping through the passage, you see a haggard man slumped\
			\nagainst a fence.\
			\n""", #+ itemTable["obsidian dagger"][2],
			items = [],
			interactions = {
				"ground" : "Broken pavement peers through damp earth.",
				"flier" : """\nThe image of a woman has been painted in a tasteful, watercolor style.\
				\nShe is wearing a black lab coat and tie, arms crossed with gray lips cut into a smile.\
				\n\n\t"Dr. Madeline Vereth's Clinic of the Clear Mind"\
				\n\n"Specializing in brain dysfunctions and mental well-being"\
				\n"If you or a loved one has experienced strange headaches, visions, sudden bleeding,\
				\ntremors, seizures, or any other mental ailment left undiagnosed, we are here to help.\
				\nOur staff is compassionate, well-trained, and ready to serve you with dignity and respect."\
				\n\n\t"A subsidiary of TEAR Bio-Enhancements"
				""",
				"garbage" : "Bags of miscellaneous refuse and crates dissolving from neglect.",
				"man" : "His chin is on his chest, the front of his button-down shirt is stained red."
			},
			connections = {"east" : "burned storehouse", "west" : "front tavern"},
			name = "Side Alley"):
		location.__init__(self, description, items, interactions, connections, name)
		
	def examine_object(self, thing):
		if thing == "garbage" and self.daggerFound == False:
			print ("""{}\
			\nBetween two of such crates, you see the hilt of\
			\nwhat appears to be a dagger.
			""".format(self.interactions["garbage"]))
			self.items.append("obsidian dagger")
			self.description += itemTable["obsidian dagger"][2]
			self.daggerFound = True
			return True
		return False

class shack(location):

####
## Metal will be an implement that player can use for incapacitating hostess
## and swaying other patrons if they have a high enough focus. If not, it can backfire
## or flat out not work.
####

	#bookD = "An old book stands out on top of the desk.\n"
	#metalD = "Shining in the lamplight, a chunk of metal lies on the ground.\n"
	cursed = False
	
	def __init__(self,
			description = """The wooden walls are stained and waterlogged.\
			\nOnce smooth clay, the floor is now closer to mud.\
			\nAn earthy smell passes through your nose and settles on your tongue.\
			\nThere is a desk, defiantly standing despite its age.\
			\n""" + itemTable["old book"][2] + itemTable["chunk of metal"][2],#bookD + metalD,
			items = ["old book", "chunk of metal"],
			interactions = {
				"figment" : "Something here."},
			connections = {"east" : "north tavern", "south" : "front tavern"},
			name = "Shack"):
		location.__init__(self, description, items, interactions, connections, name)
		
	def encounter(self):
		pass

class burnedStorehouse(location):
	def __init__(self,
			description = "Something here.",
			items = [],
			interactions = {"stuff" : "and info"},
			connections = {
				"north" : "north tavern",
				"south" : "side alley"},
			name = "Burned Storehouse"):
		location.__init__(self, description,items,interactions,connections,name)
	
class tavernEntryway(location):
	def __init__(self,
			description = """Entryway description here.
			""",
			items = [],
			interactions = ["hostess", "narrow door", "double doors", "front desk", "mail sorter"],
			connections = {"north" : "dimHallway", "east" : "The doors are shut.", "west" : "front tavern"},
			name = "Tavern Entryway"):
		location.__init__(self,description, items, interactions, connections, name)
	def closetOpen(self):
		pass
	def mailEntry(self):
		pass
	
class mainHall(location):
	def __init__(self,
			description = """Main hall description.
			""",
			items = [],
			interactions = ["guest1", "guest2", "bar", "fireplace", "artwork"],
			connections = {"north door" : "guest room 1",
				"east door left" : "locked",
				"east door right" : "guest room 2",
				"south door" : "guest room 3",
				"west" : "tavern entryway"},
			name = "Main Hall"):
		location.__init__(self, description, items, interactions, connections, name)

class guest1Room(location):
	def __init__(self,
			description = """Guest room 1 Description
			""",
			items = [],
			interactions = ["stuff"],
			connections = {"west" : "main hall"},
			name = "so-and-so's Room"):
		location.__init__(self, description, items, interactions, connections, name)

class guest2Room(location):
	def __init__(self,
			description = """Guest room 2 Description
			""",
			items = [],
			interactions = ["stuff"],
			connections = {"west" : "main hall", "east" : "window locked"},
			name = "so-and-so's Room"):
		location.__init__(self, description, items, interactions, connections, name)

class guest3Room(location):
	def __init__(self,
			description = """Guest room 3 Description
			""",
			items = [],
			interactions = ["stuff"],
			connections = {"north" : "main hall"},
			name = "so-and-so's Room"):
		location.__init__(self, description, items, interactions, connections, name)

class playerRoom(location):
	def __init__(self,
			description = """Player room Description
			""",
			items = [],
			interactions = ["stuff"],
			connections = {"south" : "tavern entryway", "secret passage" : "cellar"},
			name = "Your Room"):
		location.__init__(self, description, items, interactions, connections, name)

class cellar(location):
	def __init__(self,
			description = """Cellar Description
			""",
			items = [],
			interactions = ["stuff"],
			connections = {"west" : "main hall", "up" : "player room"},
			name = "Cellar"):
		location.__init__(self, description, items, interactions, connections, name)

class hostessRoom(location):
	def __init__(self,
			description = """Hostess room Description
			""",
			items = [],
			interactions = ["stuff"],
			connections = {"east" : "tavern entryway"},
			name = "so-and-so's Room"):
		location.__init__(self, description, items, interactions, connections, name)

####################################################
##				  --Functions--					  ##
####################################################

def game_over():
	print("You died.")
	raise SystemExit #Put core loop into a main function so that game can reset instead of quitting

trashWords = {"chunk","old","a","an","of","the","please","now"}

"""
class encounter:

	def __init__(self,name,location):
		self.name = name
		self.location = location

	def action(self,choices):
		while True:
			counter = 0
			print ("Do you...")
			for i in choices:
				counter += 1
				print("\n{}. {}\n".format(counter,i))
			choice = input(">>> ",)
			if choice in choices:
				return choice
			elif choice == "exit":
				gameExit()
			else:
				print("This is not the time to stumble...try again.")

	def stat_check(self,stat,value):
		if player.attributes[stat] >= value:
			return True
		else:
			return False

class figment(encounter):
	def __init__(self,
			name = "figment encounter",
			location = "shack"):
		encounter.__init__(self,name,location)
	def test(self):
		temp = figment
		while True:
			temp = action(temp)
			if temp == "Exit":
				return
"""
"""
def encounter(enc):
	current = enc["start"]
	while current != "Exit":
		for choice in current:
			if choice == "Prompt":
				print (current[choice])
			elif choice == "check":
				check = True
				for i in current[choice]:
					if stat_check(i[0],i[1]) is False:
						check = False
						break
				if check == True:
					current = current[choice]["passed"]
					break
				else:
					current = current[choice]["failed"]
					break
			else:
				print ("{}. {}".format(choice, current[choice][0]))
		print ("")
		pick = input(">>> ",)
		if pick in current:
			current = current[pick][1]
			break
		elif pick == "exit":
			raise SystemExit
		else:
			print ("This is not the time to stumble...try again.")
	raise SystemExit

def stat_check(stat,value):
	if player.attributes[stat] >= value:
		return True
	else:
		return False
"""

"""
class Encounter:

	def __init__(self,instance,lookup,user):
		self.user = user
		self.lookup = lookup
		self.action(instance)
	def action(self,instance):
		current = "Start"
		while current != "End":
			current = instance[current]
			current = self.parser(current)

	def parser(self, current):
		for item in current:
			if item == "Prompt":
				print (current[item])
			elif item == "Choice":
				current = self.choice(current[item])
				break
			elif item == "Check":
				checker = self.check(current[item])
				current = self.parser(current[checker])
				break
			elif item == "Return":
				self.returned(current[item])
			elif item == "Status":
				self.status(current[item])
			elif item == "Jump":
				current = current[item]
			elif item == "Exit":
				current = "End"
				break
		return current

	##Returned values function
	def returned(self,current):
		for item in current:
			if item == "Player remove":
				self.user.inv.remove(current[item])
			#elif item == "Event":
			elif "Event" in item:
				gameState.events[current[item][0]] = current[item][1]
			elif item == "return":
				pass
			elif item == "Relocate":
				newLocation = current[item]
				self.user.location = self.lookup[newLocation]

	##Choice function
	def choice(self,current):
		for item in current:
			print ("{}. {}".format(item,current[item][0]))
		while True:
			pick = input(">>> ",)
			if pick in current:
				return current[pick][1]
			else:
				print("This is not the time to stumble...try again.")

	##Check function
	def check(self, current):
		checker = True
		for item in current:
			subject = item[0]
			value = item[1]
			if subject in player.attributes:
				checker = player.attributes[subject] >= value
			elif subject == "inventory":
				checker = value in player.inv
			if checker == False:
				return "Failed"
		return "Passed"
		#Needs to handle if there is a check with no pass/fail
		#Or rephrase the dictionary to still have pass/fail
		#^^^^ Checked with the keyword inventory

	##Status function
	def status(self, current):
		for item in current:
			value = current[item]
			if item == "Player health":
				player.health += value
			elif item == "Player mental":
				player.mental_health += value
			elif item in player.condition:
				player.condition[item] = value
	def jump(self):
		pass
"""
def figmentEncounter():
	print("""\nAs you take the book from the desk,\
	\nan electric shock runs down your back.\
	\nForming from the dense air in the shack,\
	\na figure of dark purple and black energy leans forward.\
	\nTheir eyes aglow with deep crimson, they measure you.\
	\nA clawed hand extends toward you and the figment waits.
	""")
	print("Do you...")
	print("""\n1. Run\
	\n2. Give book\
	\n3. Attack!\
	\n4. Attempt to communicate
	""")
	while True:
		choice = input(">>> ",)
		if choice == "1":
			if player.attributes["dexterity"] > 7 and player.attributes["focus"] > 7:
				print ("\nA shadow falls over the shack. Eyes watch you from within.\n")
				#player.location = frontTavern()
				shack.cursed = True
				gameState.events["figment"] = False
				return "Ran"
			else:
				print("\nA claw, electric and sharp, slashes your back causing you to fall.\n")
				player.health -= 15
				print("Do you...")
				print("""\n1. Give up the book and crawl away\
				\n2.Hold on to the book and crawl away\
				\n3.Attempt an attack while prone
				""")
				choice = input(">>> ",)
				if choice == "1":
					print("\nThere is a screeching cry. When your eyes open, the figment and book are gone.\n")
					player.inv.remove("old book")
					gameState.events["figment"] = False
					player.mental_health -= 5
					return
				else:
					print("""\nThe figment lifts a claw and crushes your leg.\
					\nWhen you snap out of the pain, you find the figment\
					\nand the book gone.
					""")
					player.inv.remove("old book")
					gameState.events["figment"] = False
					player.condition["leg crippled"] = True
					player.health -= 25
					return
		elif choice == "2":
			print("""\nThe figment nods to you in appreciation.\
			\nIt dissipates, leaving no trace of itself or the book.
			""")
			player.inv.remove("old book")
			gameState.events["figment"] = False
			return
		elif choice == "3":
			print("\nHow to proceed?\n")
			print("\n1. Unarmed attack\n")
			if "dagger" in player.inv and "chunk of metal" in player.inv:
				print("""\n2. Attack with dagger\
				\n3. Concentrate on chunk of metal
				""")
			elif "dagger" in player.inv:
				print("\n2. Attack with dagger\n")
			elif "chunk of metal" in player.inv:
				print("\n2. Concentrate on chunk of metal\n")
			choice = input(">>> ",)
			if choice == "1":
				print("""\nYour fist makes contact with the body of the figment,\
				\ngoing numb and limp. As you recoil, a sharp pain erupts in your skull.
				""")
				player.mental_health -= 10
				player.health -= 10
				print("Do you...")
				print("""\n1. Run\
				\n2. Attack again\
				\n3. Give book
				""")
				choice = input(">>> ",)
				if choice == "1":
					if player.attributes["dexterity"] > 7 and player.attributes["focus"] > 7:
						print ("\nA shadow falls over the shack. Eyes watch you from within.\n")
						#player.location = frontTavern()
						shack.cursed = True
						gameState.events["figment"] = False
						return "Ran"
					else:
						print("\nA claw, electric and sharp, slashes your back causing you to fall.\n")
						player.health -= 15
						print("Do you...")
						print("""\n1. Give up the book and crawl away\
						\n2.Hold on to the book and crawl away\
						\n3.Attempt an attack while prone
						""")
						choice = input(">>> ",)
						if choice == "1":
							print("\nThere is a screeching cry. When your eyes open, the figment and book are gone.\n")
							player.inv.remove("old book")
							gameState.events["figment"] = False
							player.mental_health -= 5
							return
						else:
							print("""\nThe figment lifts a claw and crushes your leg.\
							\nWhen you snap out of the pain, you find the figment\
							\nand the book gone.
							""")
							player.inv.remove("old book")
							gameState.events["figment"] = False
							player.condition["leg crippled"] = True
							player.health -= 25
							return
				elif choice == "2":
					print("""\nYou step forward to punch again when another bolt\
					\nof pain courses through your head.\
					\nWhen it subsides and you open your eyes, the book and figment\
					\nare gone.
					""")
					player.inv.remove("old book")
					gameState.events["figment"] = False
					player.mental_health -= 10
					return
				elif choice == "3":
					print("""\nThe book is snatched from your hand.\
					\nAs the figment fades, its eyes linger a moment longer,\
					\nburning their glow into your mind.
					""")
					player.inv.remove("old book")
					gameState.events["figment"] = False
					return
			if choice == "2" and "dagger" in player.inv:
				pass
		elif choice == "4":
			pass
		else:
			print("This is not the time to stumble...try again.")

"""
##Takes a list of items and returns true if
##all of the items are in the players inventory. False otherwise.
def weapon_check(stash, weapons):
	for item in weapons:
		if item not in stash:
			return False
	return True

##Takes a dictionary with event names as keys and
##the boolean to set them to as values
def event_update(eventDict):
	for item in eventDict:
		gameState.events[item] = eventDict[item]
	return

##Takes a dictionary with numbers as keys and a list as values.
##The list values are in choice - result order
def choice(options):
	for item in options:
		print ("{}. {}".format(item,options[item][0]))
	while True:
		pick = input(">>> ",)
		if pick in options:
			return options[pick][1]
		else:
			print("This is not the time to stumble...try again.")

#def 
"""
"""
Figment encounter:

	chart = figment
	print chart[start]
	temp = choice(start choice)
	print chart[temp]
	



"""

####################################################
##				 --Encounters--					  ##
####################################################

class Encounter:
	
	def __init__(self,user,lookup):
		self.user = user
		self.lookup = lookup
		self.starter()
	def starter(self):
		pass
	def choice(self,options):
		for item in options:
			print ("{}. {}".format(item,options[item][0]))
		print("")
		while True:
			pick = input(">>> ",)
			if pick in options:
				return options[pick][1]
			else:
				print("This is not the time to stumble...try again.")
	def weapon_check(self,weapons):
		stash = self.user.inv
		for item in weapons:
			if item not in stash:
				return False
		return True
	def event_update(self,enc):
		for item in enc:
			gameState.events[item] = enc[item]
		return

class Figment(Encounter):
	
	def starter(self):
		current = figment["Start"]
		print(current["Prompt"])
		pick = self.choice(current["Choice"])
		options = {
			"Flee" : self.flee,
			"Give book calm" : self.give_book_calm,
			"Combat" : self.combat,
			"Diplomacy" : self.diplomacy
		}
		return options[pick]()
	def flee(self):
		current = figment["Flee"]
		stats = self.user.attributes
		if stats["dexterity"] > 6 and stats["focus"] > 6:
			current = current["Passed"]
			print (current["Prompt"])
			gameState.events["figment"] = False
			gameState.events["shack cursed"] = True
			self.user.location = self.lookup["front tavern"]
			return
		else:
			current = current["Failed"]
			print (current["Prompt"])
			self.user.health -= 15
			pick = self.choice(current["Choice"])
			if pick == "Crawl book":
				return self.crawl(True)
			return self.crawl(False)
	def give_book_calm(self):
		current = figment["Give book calm"]
		print (current["Prompt"])
		self.user.removeItem("old book")
		gameState.events["figment"] = False
		return
	def combat(self):
		pick = ""
		current = figment["Combat"]
		print(current["Prompt"])
		if self.weapon_check(["obsidian dagger", "chunk of metal"]):
			current = current["Passed"]
			pick = self.choice(current["Choice"])
		else:
			current = current["Failed"]
			if self.weapon_check(["obsidian dagger"]):
				pick = self.choice(current["Choice dagger"])
			elif self.weapon_check(["chunk of metal"]):
				pick = self.choice(current["Choice metal"])
			else:
				pick = self.choice(current["Choice"])
		options = {
			"Punch" : self.punch,
			"Dagger" : self.dagger,
			"Metal" : self.metal
		}
		return options[pick]()
	def diplomacy(self):
		current = figment["Diplomacy"]
		print(current["Prompt"])
		stats = self.user.attributes
		if stats["charisma"] > 4 and stats["focus"] > 6:
			current = current["Passed"]
			print(current["Prompt"])
			gameState.events["figment"] = False
			return
		current = current["Failed"]
		print(current["Prompt"])
		self.user.removeItem("old book")
		gameState.events["figment"] = False
		return
	def crawl(self, book):
		if book is False:
			current = figment["Crawl no book"]
			print(current["Prompt"])
			self.user.mental_health -= 5
		else:
			current = figment["Crawl book"]
			print(current["Prompt"])
			self.user.health -= 25
			self.user.condition["leg crippled"] = True
		self.user.removeItem("old book")
		gameState.events["figment"] = False
		return
	def punch(self):
		current = figment["Punch"]
		print(current["Prompt"])
		self.user.health -= 10
		self.user.mental_health -= 10
		pick = self.choice(current["Choice"])
		options = {
			"Flee" : self.flee,
			"Last punch" : self.last_punch,
			"Give book angry" : self.give_book_angry
		}
		return options[pick]()
	def last_punch(self):
		current = figment["Last punch"]
		print(current["Prompt"])
		self.user.mental_health -= 10
		self.user.removeItem("old book")
		gameState.events["figment"] = False
		return
	def dagger(self):
		current = figment["Dagger"]
		print(current["Prompt"])
		stats = self.user.attributes
		if stats["dexterity"] > 7 and stats["focus"] > 3:
			return self.combat_success()
		current = current["Failed"]
		print(current["Prompt"])
		self.user.mental_health -= 10
		self.user.removeItem("obsidian dagger")
		pick = self.choice(current["Choice"])
		options = {
			"Flee" : self.flee,
			"Last punch" : self.last_punch,
			"Give book angry" : self.give_book_angry
		}
		return options[pick]()
	def metal(self):
		current = figment["Metal"]
		print(current["Prompt"])
		if self.user.attributes["focus"] > 4:
			return self.combat_success()
		current = current["Failed"]
		print(current["Prompt"])
		self.user.mental_health -= 10
		pick = self.choice(current["Choice"])
		options = {
			"Flee" : self.flee,
			"Last punch" : self.last_punch,
			"Give book angry" : self.give_book_angry
		}
		return options[pick]()
	def combat_success(self):
		current = figment["Combat success"]
		print(current["Prompt"])
		self.user.mental_health -= 10
		gameState.events["figment"] = False
		return
	def give_book_angry(self):
		current = figment["Give book angry"]
		print(current["Prompt"])
		self.user.removeItem("old book")
		gameState.events["figment"] = False
		return

class Drunkard(Encounter):

	def starter(self):
		current = drunkard["Start"]
		print(current["Prompt"])
		pick = self.choice(current["Choice"])
		options = {}
		return options[pick]()
	



















