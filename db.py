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
    dk = hashlib.pbkdf2_hmac('sha256', password, salt, 10)
    return binascii.hexlify(dk)

class KeyStorage(object):
    def __init__(self):
        super(KeyStorage, self).__init__()
        self.cache = SimpleCache()

    def search(self, key):
        user = self.cache.get(key)
        return user

    def save(self, key, user, timeout=60*60):
        self.cache.set(key, user, timeout=timeout)

KeyStore = KeyStorage()