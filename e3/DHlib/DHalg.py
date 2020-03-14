from .primeGenerator import prime_generator
from lib.duty import end

noLess = 10
noMore = 20

keys = {
    'public_key_Alice': prime_generator(noLess, noMore),
    'private_key_Alice': prime_generator(noLess, noMore),
    'public_key_Bob': prime_generator(noLess, noMore),
    'private_key_Bob': prime_generator(noLess, noMore)
}

keys['partial_key_Alice'] = keys['public_key_Alice']**keys['private_key_Alice']%keys['public_key_Bob']
keys['partial_key_Bob'] = keys['public_key_Alice']**keys['private_key_Bob']%keys['public_key_Bob']
keys['full_key_Alice'] = keys['partial_key_Bob']**keys['private_key_Alice']%keys['public_key_Bob']
keys['full_key_Bob'] = keys['partial_key_Alice']**keys['private_key_Bob']%keys['public_key_Bob']

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
    if keys['full_key_Alice'] == keys['full_key_Bob']:
        return keys['full_key_Alice']
    end('Error. Keys don\'t match.')