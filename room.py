#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from flask import Blueprint, abort, request, session, jsonify
from db import DB, KeyStore

room_db = DB['rooms']
room_api = Blueprint('room_api', __name__)

@room_api.route('/room', methods=['GET', 'POST', 'PUT'])
# @room_api.route('/room/<id>', methods=['GET'])
def room(id=None):
    key = request.headers.get('key')
    user = KeyStore.search(key)
    if not user:
        return jsonify(), 401

    if request.method == 'GET':
        # Dosomething
        return jsonify(ret=user)
    

