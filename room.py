#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
    * Room API

"""

from flask import Blueprint, abort, request, session, jsonify
from db import DB, KeyStore
from bson.objectid import ObjectId
import model.rooms

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
            room = model.rooms.get_by_id(rid)
            return jsonify(status='OK', message='', data=room)
        abort(400)

    # get all user's room
    if not rid and request.method is 'GET':
        skip = request.form.get('skip',0)
        limit = request.form.get('limit',10)
        rooms = model.rooms.get(rid, skip=skip, limit=limit)
        return jsonify(status='OK', message='', data=rooms)

    # create new room
    if request.method is 'POST':
        title = request.form['title']
        user_id = user['_id'].to_s
        pin = request.form['pin']
        ret = model.rooms.add(title=title, user_id=user_id, pin=pin)
        return jsonify(status='ok', message="created", data={'room_id':ret})


    # add user to room
    if oid and request.method is 'PUT':
        user_id = request.form['user_id']
        ret = model.rooms.add_user(room_id=oid, user_id=user_id)
        if ret:
            return jsonify(status='ok', message='', data={})
        else
            abort(400)

    # user leave room
    if oid and request.method is 'DELETE':
        user_id = request.form['user_id']
        ret = model.rooms.remove_user(room_id=oid, user_id=user_id)
        if ret:
            return jsonify(status='ok', message='', data={})
        else
            abort(400)

    abort(405)
