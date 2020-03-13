import string, sys
sys.path.append('../')
from lib.colors import *
from lib.duty import *

characters = string.ascii_letters

while True:
	while True:
		text = typedText('Enter at least 10 characters or \"e\" to exit: ')

		if text == 'e' or text == 'E':
			end()
		elif len(text) >= 10:
			printTextAndValue('String is', text)
			break
		warning('You entered less than 10 characters. Please try again.')

	for character in characters:
		if(character in text):
			printTextAndValue(character, text.count(character))

	repeatProcedure()

end()