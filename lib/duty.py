from .colors import *

def repeatProcedure():
	while True:
		repeatAnswer = input('Repeat the procedure? "y" or "n": ').lower()
		if repeatAnswer == 'y':
			break
		elif repeatAnswer == 'n':
			end()

		warning('You entered wrong character. Please, try again.')

def end(text = None) -> str:
	changeColor('white')
	
	if(text):
		exit(text)
	exit('Bye bye!')

def fileNotExist(text = None) -> str:
	changeColor('red')
	print('file not exist.')
	end(text)