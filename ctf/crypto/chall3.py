import os
import sys
from Crypto.Cipher import AES

f = open('mta-flag.pdf', 'rb').read()

secret = os.urandom(16)
crypto = AES.new(os.urandom(32), AES.MODE_CTR, counter=lambda: secret)

encrypted = crypto.encrypt(f)
open('mta-flag.enc', 'wb').write(encrypted)
