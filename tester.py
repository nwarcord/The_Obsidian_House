import the_obsidian_house
import class_the_obsidian_house

input_values = ["y", "8", "2", "2", "8", "y", "n", "take book", "4", "look"]

def mock_input(s):
	if len(input_values) > 0:
		return input_values.pop(0)
	raise SystemExit
the_obsidian_house.input = mock_input
class_the_obsidian_house.input = mock_input

the_obsidian_house.main()