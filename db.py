#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from pymongo import MongoClient
import hashlib, binascii
from config import Config

client = MongoClient()

# Database
DB = client[Config['DATABASE']]

def GetUserFromToken(token):
    user = DB['users'].find_one({"token":token})
    return user

def GetHash(password):
    salt = Config['salt']
    dk = hashlib.pbkdf2_hmac('sha256', password, salt, 10)
    return binascii.hexlify(dk)