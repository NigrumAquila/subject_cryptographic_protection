from .primeGenerator import primeGenerator
from .primitiveRoot import findPrimitive
from random import randint
from lib.duty import end
from lib.colors import *

noLess = 10000
noMore = 100000

prime = primeGenerator(noLess, noMore)
generator = findPrimitive(prime)

keys = {
    'private_key_Alice': randint(noLess, noMore),
    'private_key_Bob': randint(noLess, noMore),
}

while True:
    mode = typedText('Select program mode. \
    1 - two participants communicating over an encrypted channel; \
    2 - man-in-the-middle attack: key interception and substitution; \
    3 - three participants communicating over an encrypted channel: ')
    
    if mode == '1':
        keys['public_key_Alice'] = generator ** keys['private_key_Alice'] % prime
        keys['public_key_Bob'] = generator ** keys['private_key_Bob'] % prime
        keys['shared_secret_Alice'] = keys['public_key_Bob'] ** keys['private_key_Alice'] % prime
        keys['shared_secret_Bob'] = keys['public_key_Alice'] ** keys['private_key_Bob'] % prime

        if keys['shared_secret_Alice'] != keys['shared_secret_Bob']:
            warning('Key error!')
            end()
        
        break
    if mode == '2':
        keys['private_key_Carol'] = randint(noLess, noMore)

        keys['public_key_Alice->Carol'] = generator ** keys['private_key_Alice'] % prime
        keys['public_key_Alice_Carol->Bob'] = generator ** keys['private_key_Carol'] % prime
        keys['shared_secret_key_Bob'] = keys['public_key_Alice_Carol->Bob'] ** keys['private_key_Bob'] % prime
        
        keys['public_key_Bob->Carol'] = generator ** keys['private_key_Bob'] % prime
        keys['public_key_Bob_Carol->Alice'] = generator ** keys['private_key_Carol'] % prime
        keys['shared_secret_Alice'] = keys['public_key_Bob_Carol->Alice'] ** keys['private_key_Alice'] % prime

        keys['shared_secret_Carol_Alice'] = keys['public_key_Alice->Carol'] ** keys['private_key_Carol'] % prime
        keys['shared_secret_Carol_Bob'] = keys['public_key_Bob->Carol'] ** keys['private_key_Carol'] % prime

        if keys['shared_secret_Alice'] != keys['shared_secret_Carol_Alice'] and keys['shared_secret_Bob'] != keys['shared_secret_Carol_Bob']:
            warning('Key error!')
            end()
        
        break
    if mode == '3':
        keys['private_key_Carol'] = randint(noLess, noMore)

        keys['public_key_Alice->Bob'] = generator ** keys['private_key_Alice'] % prime
        keys['public_key_Alice_Bob->Carol'] = keys['public_key_Alice->Bob'] ** keys['private_key_Bob'] % prime
        keys['shared_secret_Carol'] = keys['public_key_Alice_Bob->Carol'] ** keys['private_key_Carol'] % prime
        
        keys['public_key_Carol->Alice'] = generator ** keys['private_key_Carol'] % prime
        keys['public_key_Carol_Alice->Bob'] = keys['public_key_Carol->Alice'] ** keys['private_key_Alice'] % prime
        keys['shared_secret_Bob'] = keys['public_key_Carol_Alice->Bob'] ** keys['private_key_Bob'] % prime

        keys['public_key_Carol->Bob'] = keys['public_key_Carol->Alice']
        keys['public_key_Carol_Bob->Alice'] = keys['public_key_Carol->Bob'] ** keys['private_key_Bob'] % prime
        keys['shared_secret_Alice'] = keys['public_key_Carol_Bob->Alice'] ** keys['private_key_Alice'] % prime

        if keys['shared_secret_Alice'] != keys['shared_secret_Bob'] != keys['shared_secret_Carol']:
            warning('Key error!')
            end()

        break
    warning()



def encrypt(key: int, text: str) -> str:
    encrypted_text = ''
    for char in text:
        encrypted_text += chr(ord(char) + key)
    return encrypted_text

def decrypt(key: int, text: str) -> str:
    decrypted_text = ''
    for char in text:
        decrypted_text += chr(ord(char) - key)
    return decrypted_text

def getSharedSecret() -> int:
    return keys['shared_secret_Alice']

def printAllKeys():
    for key, value in keys.items():
        printTextAndValue(key, value)

def printParams():
    printTextAndValue('prime = ', prime)
    printTextAndValue('generator = ', generator)