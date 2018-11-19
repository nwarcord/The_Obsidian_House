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
		self.inv.append(thing)
		self.location.interactions[thing] = "{} is no longer here.".format(thing)
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
						self.pickAttributes()
					else:
						print("I didn't catch that.")
		if total != 0:
			print("\nYou failed to use all of your points. Try again.")
			self.pickAttributes()
	def printLocation(self):
		self.location.printDescription()
	def printInv(self):
		print ("\nYour pockets contain:\n")
		for i in self.inv:
			print ("\t",i.name)
		print("")
		
		#if self.location.visited == False:
			#self.location.printDescription()
			#self.location.visited = True
		#else:
			#print("\n"+"--"+self.location.name+"--")

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
		print("\n"+"--"+self.name+"--")
		print (self.description)
	def printInteractions(self, thing):
		if i in interactions:
			print (interactions[i])

class item:
	
	def __init__(self,description,name):
		self.description = description
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
			description = """\nSomething is here.
			""",
			interactions = {
				"sign" : "Sign description",
				"ground" : "Ground description",
				"door" : "Door description",
				"river" : "River description"},
			connections = {
				"north" : "shack",
				"south" : "sideAlley",
				"east" : "player.location.doorOpen()"},
				name = "Front Tavern"):
		location.__init__(self,description,interactions,connections,name)
		
	def doorOpen(self):
		print("The door is shut.")
		cmmd = input(">>> ",)
		if cmmd.lower() == "open door":
			self.connections["east"] = "tavernEntryway"
			interactions["door"] = "Warm light and soft music spill from the doorway."
			print ("You turn the cold, silver handle until there is a satisfying click. The door opens smooth and silent.")
			self.description += "\nThe door to the building is open."
		else:
			return cmmd

class northTavern(location):
	def __init__(self,
			description = """\nAnother description here.
			""",
			interactions = ["ground", "window", "trap door"],
			connections = {"west" : "shack", "east": "burnedStorehouse"}):
		location.__init__(self, description, interactions, connections)

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
			connections = {"east" : "burnedStorehouse", "west" : "frontTavern"}):
		location.__init__(self, description, interactions, connections)
	
class shack(location):

####
## Metal will be an implement that player can use for incapacitating hostess
## and swaying other patrons if they have a high enough focus. If not, it can backfire
## or flat out not work.
####

	def __init__(self,
			description = """Shack description.
			""",
			interactions = ["book", "strange metal", "figment"],
			connections = {"east" : "northTavern", "south" : "frontTavern"}):
		location.__init__(self, description, interactions, connections)

class burnedStorehouse(location):
	pass
	
class tavernEntryway(location):
	def __init__(self,
			description = """Entryway description here.
			""",
			interactions = ["hostess", "narrow door", "double doors", "front desk", "mail sorter"],
			connections = {"north" : "dimHallway", "east" : "The doors are shut.", "west" : "frontTavern"}):
		location.__init__(self,description, interactions, connections)
	def closetOpen(self):
		pass
	def mailEntry(self):
		pass
	
class mainHall(location):
	def __init__(self,
			description = """Main hall description.
			""",
			interactions = ["guest1", "guest2", "bar", "fireplace", "artwork"],
			connections = {"north door" : "guest1Room",
			"east door left" : "locked",
			"east door right" : "guest2Room",
			"south door" : "guest3Room",
			"west" : "tavernEntryway"}):
		location.__init__(self, description, interactions, connections)

class guest1Room(location):
	def __init__(self,
			description = """Guest room 1 Description
			""",
			interactions = ["stuff"],
			connections = {"west" : "mainHall"}):
		location.__init__(self, description, interactions, connections)

class guest2Room(location):
	def __init__(self,
			description = """Guest room 2 Description
			""",
			interactions = ["stuff"],
			connections = {"west" : "mainHall", "east" : "window locked"}):
		location.__init__(self, description, interactions, connections)

class guest3Room(location):
	def __init__(self,
			description = """Guest room 3 Description
			""",
			interactions = ["stuff"],
			connections = {"north" : "mainHall"}):
		location.__init__(self, description, interactions, connections)

class playerRoom(location):
	def __init__(self,
			description = """Player room Description
			""",
			interactions = ["stuff"],
			connections = {"south" : "tavernEntryway", "secret passage" : "cellar"}):
		location.__init__(self, description, interactions, connections)

class cellar(location):
	def __init__(self,
			description = """Cellar Description
			""",
			interactions = ["stuff"],
			connections = {"west" : "mainHall", "up" : "playerRoom"}):
		location.__init__(self, description, interactions, connections)

class hostessRoom(location):
	def __init__(self,
			description = """Hostess room Description
			""",
			interactions = ["stuff"],
			connections = {"east" : "tavernEntryway"}):
		location.__init__(self, description, interactions, connections)

####################################################
##				    --Items--					  ##
####################################################

class strangeToken(item):
	def __init__(self,
			description = "A cold stone with a rune on it.",
			name = "Strange Token"):
		item.__init__(self,description,name)

itemList = {
	"strange token" : strangeToken()
}

####################################################
##				  --Functions--					  ##
####################################################

def eventTracker():
	pass