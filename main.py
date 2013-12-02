"""
Alveyworld-dev calculator
Period 6

Shrek is love. Shrek is life. Shrek is Alveyworld. All hail Shrek.

Group 1: Team Jacob
Members:
	* Jared
	* Josh
	* Max
	* Santiago
	* Travis
"""

# Raw imports
import shlex
import math
import random

# Class Imports
import team1
# import team2
# import team3
# import team4
# import team5
# import team6

class colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


if __name__ == "__main__":
	"""
	Main entry point for the program
	"""
	
	print "Alveyworld Calculator"
	print "Copyright 2013, Alvey's Class\n"

	# Defines a set of commands that
	# are used for the command interpreter
	commands = {
		"exit",
		"sqrt",
		"abs",
		"fact",
		"pow",
		"ln",
		"mod",
		"log10",
		"divide",
		"multiply",
		"inverse",
		"add",
		"sub",
		"opp",
		"hello"
	}

	# Whitty responses for the command "hello"
	hellos = [
		"hello, puny human",
		"my other car is siri",
		"feed me paper",
		"khaaaaaaaaaannn!",
		"fight me mcpunches",
		"fight me irl n00b",
		"1v1 me",
		"shrek is life.  shrek is love",
		"the machine race rises"
	]

	while True:
		command = shlex.split(raw_input("> "))
		cmd = command[0]

		for _cmd in commands:
			if _cmd == cmd:
				if cmd == "sqrt":
					number = int(command[1])
					print(team1.sqrt(number))
				elif cmd == "exit":
					exit(0)
				elif cmd == "hello":
					print(hellos[random.randint(0, len(hellos) - 1)])



