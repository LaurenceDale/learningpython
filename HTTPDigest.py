#!/usr/bin/python

#HTTP Digest authentication script.
#Digest authentication works as follows: hash1 is MD5 a hash of the inputs ('username:realm:password')
# hash2 is MD5 hash of (method:uri)
# the response hash is MD5 of (hash1:nonce:hash2) where the nonce is a unique value provided by server. Session ID esque

import hashlib

hash1 = hashlib.md5('admin:PentesterAcademy:asdds').hexdigest()

hash2 = hashlib.md5('GET:/lab/webapp/digest/1').hexdigest()

response_string = hash1 + ':' + nonce + ':' + hash2

response = hashlib.md5(response_string).hexdigest()
