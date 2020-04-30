import __main__
if __main__.__file__ != 'main.py':
    exit('run main.py')

from .DHlib.DHalg import encrypt, decrypt, getSharedSecret, printAllKeys, printParams
from lib.colors import *
from lib.duty import *

key = getSharedSecret()
printAllKeys()

while True:
    
    printParams();
    message = typedText('Enter message for RSA encryption: ')
    printTextAndValue('Original message: ', message)
    
    encrypted_message = encrypt(key, message)
    try:
        printTextAndValue('Encrypted message: ', encrypted_message)
    except UnicodeError:
        warning('\rYour encoding isn\'t UTF-8')
        end('Please, restart it with "PYTHONIOENCODING=UTF-8 python main.py" or by IDE with utf8 encoding')

    decrypted_message = decrypt(key, encrypted_message)
    printTextAndValue('Decrypted message: ', decrypted_message)
    
    repeatProcedure()