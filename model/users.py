# -*- coding: utf-8 -*-

# Title: Exception class
# Author: Pongsakorn Sommalai
# Descripter: Exception class
# Date 11/02/2016

from pymongo import MongoClient
from config import Config

client = MongoClient()

users = client[Config['DATABASE']]["users"]

def login(token):
	return users.find_one({"token": token})

def add(token, name, fullname, email, image):
	users.insert_one({"name": name, "fullname": fullname, "email": email, "image": image, "token": token, "create_ts": time.time()})

def get(search, skip=0, limit=10, s=1):
	return list(users.find(filter={"$or": [{"name": '/'+search+'/'}, {"fullname": '/'+search+'/'}, {"email": '/'+search+'/'}]}, skip=skip, limit=limit).sort('name', pymongo.DESCENDING))
