"""
Alveyworld-dev calculator
Period 6

Shrek is love. Shrek is life.

Group 1: Team Jacob
Members:
	* Jared
	* Josh
	* Max
	* Santiago
	* Travis
"""

# Imports
import group1

class colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def check_commands(command, *arguments):
	"""
	Checks user-entered commands
	"""

	commands = {
		"exit"
	}

	for _command in commands:
		if _command == command:
			print _command
		else:
			print colors.FAIL + "Error, command \"" + command + "\" not found" + colors.ENDC

	pass

if __name__ == "__main__":
	"""
	Main entry point for the program
	"""
	
	print "Alveyworld Calculator"
	print "Copyright 2013, Alvey's Class\n"

	while True:
		check_commands(raw_input("> "), None)
