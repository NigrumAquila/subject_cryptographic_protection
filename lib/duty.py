from .colors import *

def repeatProcedure():
	while True:
		repeatAnswer = input('Repeat the procedure? "y" or "n": ').lower()
		if repeatAnswer == 'y':
			break
		elif repeatAnswer == 'n':
			end()

		warning()

def end(text: str = None):
	changeColor('white')
	
	if(text):
		exit(text)
	exit('Bye bye!')

def fileNotExist(text: str = None):
	changeColor('red')
	print('file not exist.')
	end(text)