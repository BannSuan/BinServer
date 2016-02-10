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

def add(token, name="", fullname="", email="", image=""):
	users.insert_one({"name": name, "fullname": fullname, "email": email, "image": image, "token": token, "create_ts": time.time()})

def update(token, name, fullname, email, image):
	return users.update_one({"name": name, "fullname": fullname, "email": email, "image": image}, {"token": token}).modified_count==1

def search(search, skip=0, limit=10):
	if limit>50:
		limit = 50

	return list(users.find(filter={"$or": [{"name": '/'+search+'/'}, {"fullname": '/'+search+'/'}, {"email": '/'+search+'/'}]}, skip=skip, limit=limit).sort('name', pymongo.DESCENDING))

def get(uid):
	return users.find_one({"_id": uid})
