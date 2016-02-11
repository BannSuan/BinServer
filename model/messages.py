# -*- coding: utf-8 -*-


from pymongo import MongoClient
from config import Config
from bson.objectid import ObjectId
import time

client = MongoClient()

messages = client[Config['DATABASE']]["messages"]

def add(data, room_id, user_id):
    messages.insert_one({
        "data": data,
        "room_id": room_id, 
        "user_id": user_id, 
        "create_ts": time.time()
    })

def get_by_room(room_id, skip=0, limit=10):
    return list(messages.find(filter={'room_id':ObjectId(room_id)}, skip=skip, limit=limit).sort('create_ts', pymongo.DESCENDING))

def get(message_id):
    return message.find_one({'_id': ObjectId(message_id)})

