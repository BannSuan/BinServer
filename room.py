#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
    * Room API

"""

from flask import Blueprint, abort, request, session, jsonify
from db import DB, KeyStore
from bson.objectid import ObjectId

room_db = DB['rooms']
room_api = Blueprint('room_api', __name__)

@room_api.route('/room', methods=['GET', 'POST'])
@room_api.route('/room/<oid>', methods=['GET','DELETE','PUT'])
def room(rid=None):
    key = request.headers.get('x-key')
    user = KeyStore.search(key)
    if not user:
        abort(401)

    # get room info
    if rid and request.method is 'GET':
        if ObjectId(oid) in user['rooms']:
            room = room_db.findOne({'_id': ObjectId(rid)})
            return jsonify(status='OK', message='', data=room)
        abort(400)

    # get all user's room
    if rid and request.method is 'GET':
        rooms = room_db.find({"_id":{"$in":user["room_id"]}})
        return jsonify(status='OK', message='', data=[])

    # create new room
    if request.method is 'POST':
        title = request.form['title']


    # add user to room
    if request.method is 'PUT':
        pass

    # user leave room
    if request.method is 'DELETE':
        pass

    abort(405)

    return NotImplemented()
