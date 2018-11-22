import re
import regex
from bitarray import bitarray
from class_the_obsidian_house import *

cmdExit = re.compile(("^(Quit|Exit){1}$"),re.I)
cmdInv = re.compile("^(Inventory){1}$",re.I)
cmdScan = re.compile(("^(Scan|Look){1}$"),re.I)
cmdHelp = re.compile(("^(Help){1}$"),re.I)
cmdMove = re.compile(r"^(n|north|s|south|e|east|w|west|up|down){1}$",re.I)
cmdOpen = re.compile(("^Open\s(\w+)$"),re.I)

def user_input(cmmd):
	cmdExamine = regex.search(r"(?<=Examine\s)((\w+)(?:\s)*)+",cmmd,regex.I)
	if cmdExit.search(cmmd):
		gameExit()
	elif cmdInv.search(cmmd):
		player.printInv()
	elif cmdExamine:
		temp = cmdExamine.captures()
		temp = "".join(temp)
		if temp in player.location.interactions:
			print(player.location.interactions[temp])
			return
		for i in player.location.interactions:
			if i in temp:
				print(player.location.interactions[i])
				return
		print("You can't do that.")
	elif cmdOpen.match(cmmd):
		x = cmdOpen.match(cmmd)
		player.location.openObject(x.group(1))
	elif cmdMove.search(cmmd):
		failed = str(player.location)
		player.playerMove(cmmd,lookupTable)
		if str(player.location) == failed:
			return
		visit = player.location.visited
		player.printLocation(visit)
		player.location.visited = True
	elif cmdScan.search(cmmd):
		player.printLocation(False)
	elif cmdHelp.search(cmmd):
		printCommands()
	elif cmmd == "stop":
		gameExit()
	else:
		print("\nI don't know that command.\n")
	return

def printCommands():
	print("""\n[Quit or Exit] = Close the game\
	\n\nInventory = Print the contents of your inventory\
	\n\n[Scan or Look] = Print the description of your surroundings.\
	\n\nNote: Commands are not case-sensitive.
	\n""")

def welcomeMsg():
	print ("""\
	\n------------------------------------\
	\nHello and welcome to Obsidian House!\
	\nWe hope you enjoy your...time...\
	\n------------------------------------\
	
	\nType "Help" at anytime to print the command list.
	\n""")
	
	count = 0
	while True:
		cmmd = input("Would you like to start the game? (Yes/No): ",).lower()
		if cmmd == "yes" or cmmd == "y":
			return
		elif cmmd == "no" or cmmd == "n":
			gameExit()
		else:
			if count == 0:
				print("""\nI didn't catch that.
				""")
			elif count == 1:
				print("""\nCome again?
				""")
			elif count == 2:
				print("""\nAre you serious right now?
				""")
			elif count == 3:
				print("""\nReally?
				""")
			elif count == 4:
				print("""\nOh, come on.
				""")
			elif count == 5:
				print("""\nNow you're just doing it to see how long I can keep this up.
				""")
			elif count == 6:
				print("""\nWell I have all the time in the world buddy.
				""")
			elif count == 7:
				print("""\nBring it.
				""")
			elif count in range(8,11):
				print("""\nStill going.
				""")
			elif count == 11:
				print("""\nOkay okay okay. Are we seriously going to do this?
				""")
			elif count == 12:
				print("""\nWell I guess we are.
				""")
			elif count == 13:
				print("""\nIf you insist.
				""")
		count += 1

def gameExit():
	print("""
	"When humans speak of fear,
	I shake my head in pity.
	To see stars consumed and reality as you know it torn...
	No. They speak out of ignorance. Let us hope they remain comfortably so."
		-- Lira, of the Crimson Marsh - C.S.E. to Earth, 1802 C.E.
	""")
	raise SystemExit	

frontTavern = frontTavern()
shack = shack()
northTavern = northTavern()
tavernEntryway = tavernEntryway()
sideAlley = sideAlley()
burnedStorehouse = burnedStorehouse()
mainHall = mainHall()
guest1Room = guest1Room()
guest2Room = guest2Room()
guest3Room = guest3Room()
playerRoom = playerRoom()
cellar = cellar()
hoshostessRoom = hostessRoom()	
player = player(frontTavern,strangeToken())

lookupTable = {

	"shack" : shack,
	"front tavern" : frontTavern,
	"north tavern" : northTavern,
	"tavern entryway" : tavernEntryway,
	"side alley" : sideAlley,
	"burned storehouse" : burnedStorehouse,
	"main hall" : mainHall,
	"guest room 1" : guest1Room,
	"guest room 2" : guest2Room,
	"guest room 3" : guest3Room,
	"player room" : playerRoom,
	"cellar" : cellar,
	"hostess room" : hostessRoom
}

welcomeMsg()
#player.pickAttributes()
#player.printAttributes()
print("-"*52)
print(player.location.description)
player.location.visited = True
while True:
	user_input(input(">>> ",))