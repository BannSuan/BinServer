#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from pymongo import MongoClient
import hashlib, binascii
from config import Config
from werkzeug.contrib.cache import SimpleCache
import random

client = MongoClient()

# Database
DB = client[Config['DATABASE']]

def GenerateKey(length=32):
    return ''.join([ random.choice("0123456789ABCDEF") for i in range(length)])

def GetHash(password):
    salt = Config['salt']
    dk = hashlib.pbkdf2_hmac('sha256', password, salt, 2)
    return binascii.hexlify(dk)

class KeyStorage(object):
    def __init__(self):
        super(KeyStorage, self).__init__()
        self.cache = dict()

    def search(self, key):
        user = self.cache.get(key)
        return user

    def save(self, key, user):
        self.cache[key] = user
        
    def delete(self, key):
        try:
            del self.cache[key]
        except Exception, e:
            pass
        

KeyStore = KeyStorage()