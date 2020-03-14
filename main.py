from lib.colors import *
from lib.duty import *

exercises = ['countSymbols', 'hashAlg', 'DiffieHellman']

print('Exercise list:')
for idx, exercise in enumerate(exercises):
	printTextAndValue(str(idx + 1), exercise)

while True:
	
	choise = input('Select exercise number or enter "e" to exit: ')
	
	if choise.isdigit():
		choise = int(choise) 
		
		if choise > 0 and choise <= len(exercises):
			command = 'from e%s.%s import *' % (choise, exercises[choise-1])
			exec(command)
	if choise == 'e':
		end()

	warning()