#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
    * Room API

"""

from flask import Blueprint, abort, request, session, jsonify
from db import DB, KeyStore

room_db = DB['rooms']
room_api = Blueprint('room_api', __name__)

@room_api.route('/room', methods=['GET', 'POST', 'PUT'])
@room_api.route('/room/<id>', methods=['GET'])
def room(id=None):
    key = request.headers.get('x-key')
    user = KeyStore.search(key)
    if not user:
        return jsonify(status="fail", msg="UNAUTHORIZED", data={}), 401

    return NotImplemented()
