from .primeGenerator import prime_generator
from lib.duty import end
from lib.colors import *

noLess = 10000
noMore = 100000

keys = {
    'public_key_Alice': prime_generator(noLess, noMore),
    'private_key_Alice': prime_generator(noLess, noMore),
    'public_key_Bob': prime_generator(noLess, noMore),
    'private_key_Bob': prime_generator(noLess, noMore)
}

while True:
    mode = typedText('Select program mode. 1 - two participants communicating over an encrypted channel; 2 - man-in-the-middle attack: ')
    if mode == '1':
        keys['partial_key_Alice'] = keys['public_key_Alice'] ** keys['private_key_Alice'] % keys['public_key_Bob']
        keys['partial_key_Bob'] = keys['public_key_Alice'] ** keys['private_key_Bob'] % keys['public_key_Bob']
        keys['full_key_Alice'] = keys['partial_key_Bob'] ** keys['private_key_Alice']%keys['public_key_Bob']
        keys['full_key_Bob'] = keys['partial_key_Alice'] ** keys['private_key_Bob'] % keys['public_key_Bob']

        if keys['full_key_Alice'] != keys['full_key_Bob']:
            warning('Key error!')
            end()
        
        break
    if mode == '2':
        keys['private_key_Carol'] = prime_generator(noLess, noMore)
        
        keys['partial_key_Alice->Bob'] = keys['public_key_Alice'] ** keys['private_key_Alice'] % keys['public_key_Bob']
        keys['partial_key_Alice_Bob->Carol'] = keys['partial_key_Alice->Bob'] ** keys['private_key_Bob'] % keys['public_key_Bob']
        keys['full_key_Carol'] = keys['partial_key_Alice_Bob->Carol'] ** keys['private_key_Carol'] % keys['public_key_Bob']
        
        keys['partial_key_Carol->Alice'] = keys['public_key_Alice'] ** keys['private_key_Carol'] % keys['public_key_Bob']
        keys['partial_key_Carol_Alice->Bob'] = keys['partial_key_Carol->Alice'] ** keys['private_key_Alice'] % keys['public_key_Bob']
        keys['full_key_Bob'] = keys['partial_key_Carol_Alice->Bob'] ** keys['private_key_Bob'] % keys['public_key_Bob']

        keys['partial_key_Carol->Bob'] = keys['partial_key_Carol->Alice']
        keys['partial_key_Carol_Bob->Alice'] = keys['partial_key_Carol->Bob'] ** keys['private_key_Bob'] % keys['public_key_Bob']
        keys['full_key_Alice'] = keys['partial_key_Carol_Bob->Alice'] ** keys['private_key_Alice'] % keys['public_key_Bob']

        if keys['full_key_Alice'] != keys['full_key_Bob'] != keys['full_key_Carol']:
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

def getFullKey() -> int:
    return keys['full_key_Alice']

def printAllKeys() -> dict:
    for key, value in keys.items():
        printTextAndValue(key, value)