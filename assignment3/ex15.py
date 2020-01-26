# commands the linbe to accept a command to read a file
from sys import argv

# format of the command by first running this script and then what target to read
script, filename = argv

# says what to open
txt = open(filename)

# prints the phrase
print(f"Here's your file {filename}:")
# prints the contents of the file to be read
print(txt.read())

# redundant print
# print("Type the filename again:")
# requires input to open either the current file again or to look for a different file
# file_again = input("> ")

# repeats the open command
# txt_again = open(file_again)

# prints the contents of the file again.
# print(txt_again.read())
