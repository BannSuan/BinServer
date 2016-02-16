#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from pymongo import MongoClient
from config import Config
import random
import bcrypt
import hmac

client = MongoClient()

# Database
DB = client[Config['DATABASE']]

def GenerateKey(length=32):
    return ''.join([ random.choice("0123456789ABCDEF") for i in range(length)])

def GetHash(password):
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    # return hashed
    return password

def validPassword(password, hashed):
    return hmac.compare_digest(bcrypt.hashpw(password, hashed), hashed)

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