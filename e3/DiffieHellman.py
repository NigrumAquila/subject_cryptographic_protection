import __main__
if __main__.__file__ != 'main.py':
    exit('run main.py')

from .DHlib.DHalg import encrypt, decrypt, getFullKey
from lib.colors import *
from lib.duty import *

key = getFullKey()

while True:
    message = typedText('Enter message for RSA encryption: ')
    printTextAndValue('Original message: ', message)
    
    encrypted_message = encrypt(key, message)
    printTextAndValue('Encrypted message: ', encrypted_message)

    decrypted_message = decrypt(key, encrypted_message)
    printTextAndValue('Decrypted message: ', decrypted_message)
    
    repeatProcedure()