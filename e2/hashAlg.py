import os, hashlib, zlib, sys
sys.path.append('../')
from lib.colors import *
from lib.duty import *

def encode(algorythms: [str]):

	for algorythm in algorythms:
		command = 'hashlib.%s(text).hexdigest()' %algorythm
		printText(algorythm.upper())
		printValue(eval(command))

	printText('Adler32')
	printValue(str(zlib.adler32(text)))

while True:
	while True:
		choise = input('Select encoding source.\nFile or string?\nPress \"f\" or \"s\" and enter. \"e\" to exit: ').lower()

		if choise == 'f':
			encodingFile = input("Enter filename or leave the field blank to check encoding.txt: ") or 'encoding.txt'
			text = open(encodingFile, 'r').read().encode() if os.path.isfile(encodingFile) else fileNotExist()
			break
		elif choise == 's':
			text = typedText('Enter string: ').encode()
			break
		elif choise == 'e':
			end()
			break

		warning()

	encode(['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'])

	repeatProcedure()