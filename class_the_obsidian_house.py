from bitarray import bitarray

####################################################
##				  --Classes--					  ##
####################################################

class player:
	
	attributes = {
		"charisma" : 0,
		"strength" : 0,
		"dexterity" : 0,
		"focus" : 0
	}
	inv = []
	health = 100
	mental_health = 100
	condition = {
		"arm_broken" : False,
		"leg_broken" : False,
		"eye_blinded" : False,
		"tongue_removed" : False
	}
	
	def __init__(self,location,item):
		self.location = location
		self.inv.append(item)
	def takeItem(self, thing):
		self.inv.append(itemList[thing])
		print("\nYou take the {}.".format(thing))
		#self.location.interactions[thing] = "{} is no longer here.".format(thing)
	def printAttributes(self):
		#print("\nYour attributes are:\n")
		for i in self.attributes:
			#print("\n" + i + " = " + self.attributes[i])
			print("{} = {}\n".format(i, self.attributes[i]))
	def pickAttributes(self):
		total = 20
		pick = 0
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
			print ("\t-",i.name)
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

class location:
	
	visited = False
	
	def __init__(self, description, interactions, connections, name):
		self.description = description
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
	def takeObject(self, thing):
		print ("\nThere is no {} to take.\n".format(thing))

class item:
	
	def __init__(self,description,location,name):
		self.description = description
		self.location = location
		self.name = name
	#description = ""
	#location = ""
	#event_changes = {}

class gameState:

	events = {
		0 : "nighttime"
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

####################################################
##				  --Locations--				  	  ##
####################################################

class frontTavern(location):

	def __init__(self,
			description = """\nThe air at dusk is humid on the edge of the -blank- River.\
			\nYou stand outside of a wooden building, the river at your back.\
			\nThe gray paint is chipping, but the structure appears sturdy.\
			\nThere is a sign above the door.\n""",
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
		location.__init__(self,description,interactions,connections,name)
		
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
			description = """\nAnother description here.
			""",
			interactions = ["ground", "window", "trap door"],
			connections = {"west" : "shack", "east": "burned storehouse"},
			name = "North Tavern"):
		location.__init__(self, description, interactions, connections, name)

class sideAlley(location):

####
## Garbage will contain a dagger made of dark stone.
## If player is fast enough, they can use the dagger efficiently.
## If they are strong enough, they can use the dagger to finish an enemy
## (but not very well if they try to use it to start off as they will be slow.
## They would have to beat someone first.)
####

	def __init__(self,
			description = """Side alley description.
			""",
			interactions = ["ground", "papers", "garbage"],
			connections = {"east" : "burned storehouse", "west" : "front tavern"},
			name = "Side Alley"):
		location.__init__(self, description, interactions, connections, name)
	
class shack(location):

####
## Metal will be an implement that player can use for incapacitating hostess
## and swaying other patrons if they have a high enough focus. If not, it can backfire
## or flat out not work.
####

	def __init__(self,
			description = """Shack description.
			""",
			interactions = {
				"book" : """\nLeather-bound and crisp.\
				\nThe elements have had no effect on its condition.
				""",
				"strange metal" : "\nDark and cold.\n",
				"figment" : "Something here."},
			connections = {"east" : "north tavern", "south" : "front tavern"},
			name = "Shack"):
		location.__init__(self, description, interactions, connections, name)
		
	def takeObject(self, thing):
		if thing == "book" and self.interactions[thing] != "Gone":
			self.interactions[thing] = "Gone"
			return True
		else:
			print ("There is no {} here to take.".format(thing))
			return False

class burnedStorehouse(location):
	def __init__(self,
			description = "Something here.",
			interactions = {"stuff" : "and info"},
			connections = {
				"north" : "north tavern",
				"south" : "side alley"},
			name = "Burned Storehouse"):
		location.__init__(self, description,interactions,connections,name)
	
class tavernEntryway(location):
	def __init__(self,
			description = """Entryway description here.
			""",
			interactions = ["hostess", "narrow door", "double doors", "front desk", "mail sorter"],
			connections = {"north" : "dimHallway", "east" : "The doors are shut.", "west" : "front tavern"},
			name = "Tavern Entryway"):
		location.__init__(self,description, interactions, connections, name)
	def closetOpen(self):
		pass
	def mailEntry(self):
		pass
	
class mainHall(location):
	def __init__(self,
			description = """Main hall description.
			""",
			interactions = ["guest1", "guest2", "bar", "fireplace", "artwork"],
			connections = {"north door" : "guest room 1",
				"east door left" : "locked",
				"east door right" : "guest room 2",
				"south door" : "guest room 3",
				"west" : "tavern entryway"},
			name = "Main Hall"):
		location.__init__(self, description, interactions, connections, name)

class guest1Room(location):
	def __init__(self,
			description = """Guest room 1 Description
			""",
			interactions = ["stuff"],
			connections = {"west" : "main hall"},
			name = "so-and-so's Room"):
		location.__init__(self, description, interactions, connections, name)

class guest2Room(location):
	def __init__(self,
			description = """Guest room 2 Description
			""",
			interactions = ["stuff"],
			connections = {"west" : "main hall", "east" : "window locked"},
			name = "so-and-so's Room"):
		location.__init__(self, description, interactions, connections, name)

class guest3Room(location):
	def __init__(self,
			description = """Guest room 3 Description
			""",
			interactions = ["stuff"],
			connections = {"north" : "main hall"},
			name = "so-and-so's Room"):
		location.__init__(self, description, interactions, connections, name)

class playerRoom(location):
	def __init__(self,
			description = """Player room Description
			""",
			interactions = ["stuff"],
			connections = {"south" : "tavern entryway", "secret passage" : "cellar"},
			name = "Your Room"):
		location.__init__(self, description, interactions, connections, name)

class cellar(location):
	def __init__(self,
			description = """Cellar Description
			""",
			interactions = ["stuff"],
			connections = {"west" : "main hall", "up" : "player room"},
			name = "Cellar"):
		location.__init__(self, description, interactions, connections, name)

class hostessRoom(location):
	def __init__(self,
			description = """Hostess room Description
			""",
			interactions = ["stuff"],
			connections = {"east" : "tavern entryway"},
			name = "so-and-so's Room"):
		location.__init__(self, description, interactions, connections, name)

####################################################
##				    --Items--					  ##
####################################################

class strangeToken(item):
	def __init__(self,
			description = "A cold stone with a rune on it.",
			location = "player",
			name = "Strange Token"):
		item.__init__(self,description,name)

class oldBook(item):
	def __init__(self,
			description = """Leather-bound and crisp.\
			\nThe elements have had no effect on its condition.
			""",
			location = "shack",
			name = "Old Book"):
		item.__init__(self,description,name)

itemList = {
	"strange token" : strangeToken(),
	"book" : oldBook()
}

####################################################
##				  --Functions--					  ##
####################################################

def eventTracker():
	pass