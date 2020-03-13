class colors:
	default = '\033[39m'
	black = '\033[30m'
	gray = '\033[90m'
	red = '\033[91m'
	green = '\033[92m'
	yellow = '\033[93m'
	blue = '\033[94m'
	magenta = '\033[95m'
	cyan = '\033[96m'
	white = '\033[97m'

print(colors.green, end = '')

def changeColor(color: str):
	command = 'colors.%s' %color
	print(eval(command), end = '')

def defaultColor():
	changeColor('green')

def warning(text: str = 'You entered wrong character. Please, try again.'):
	changeColor('red')
	print(text)
	defaultColor()

def printText(text: str = None):
	changeColor('magenta')
	print(text)
	defaultColor()

def printValue(text: str = None):
	changeColor('blue')
	print(text)
	defaultColor()

def printTextAndValue(text: str, value: str):
	changeColor('magenta')
	print(text + ': ', end = '')
	changeColor('white')
	print(value)
	defaultColor()

def typedText(text: str = None) -> str:
	changeColor('yellow')
	print(text, end = '')
	changeColor('cyan')
	typedText = input()
	defaultColor()
	return typedText