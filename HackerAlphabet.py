import sys

orgText = ""
hackText = ""

# Functions

def makeHack(letter):
	global hackText
	lettersOrig = ["O","A","B","I","T","G","E","S","Z"]
	lettersRepl = ["0","4","8","1","7","6","3","5","2"]

	letter = letter.upper()

		if letter in lettersOrig :
			hackText += lettersRepl[lettersOrig.index(letter)]
		else :
			hackText += letter

if len(sys.argv) < 2 :
	print("please provide text-file as argument")
else : 
	f = open(sys.argv[1], "r")
	orgText = f.read()

for x in orgText:
	makeHack(x)
   
print(hackText)

