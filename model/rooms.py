# -*- coding: utf-8 -*-


from pymongo import MongoClient
from config import Config
from bson.objectid import ObjectId
import time

client = MongoClient()

rooms = client[Config['DATABASE']]["rooms"]

def add(title, pin, user_id):
    return messages.insert_one({
        'title': title,
        'pin': pin, 
        'users_id': [ObjectID(user_id),],
        'last_message_by': ObjectID(user_id),
        'create_ts': time.time(),
        'update_ts': time.time()
    })

def get_by_id(room_id):
    return rooms.find_one({'_id':ObjectID(room_id)})

def get(user_id, skip=0, limit=10):
    return list(rooms.find(
                filter={
                    "users_id":{"$in":[ ObjectID(user_id)]}
                    }, 
                skip=skip, 
                limit=limit
            )).sort('update_ts', pymongo.DESCENDING)

def add_user(room_id, user_id):
    return rooms.update_one({'_id': ObjectID(room_id)},
                {
                    '$addToSet':{
                        'users_id':ObjectID(user_id)
                    }
                }
            ).modified_count==1

def remove_user(room_id, user_id):
    ret = rooms.update_one({'_id': ObjectID(room_id)},
                {
                    '$pull':{
                        'users_id':ObjectID(user_id)
                    }
                }
            ).modified_count==1
    if len(ret['users_id']) == 0:
        rooms.delete_one({'_id':ObjectID(room_id)})
    return ret

def noti(room_id, user_id):
    return rooms.update_one({'_id': ObjectID(room_id)},
                {
                    '$set':{
                        'last_message_by':ObjectID(user_id),
                        'update_ts': time.time()
                    }
                }
            ).modified_count==1

