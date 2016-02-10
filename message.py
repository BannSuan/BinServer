#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
    * Message API

"""

from flask import Blueprint, abort, request, session, jsonify
from db import DB, KeyStore

message_db = DB['messages']
message_api = Blueprint('message_api', __name__)

@message_api.route('/message', methods=['GET', 'POST', 'PUT'])
@message_api.route('/message/<id>', methods=['GET', 'POST'])
def message(id=None):
    key = request.headers.get('x-key')
    user = KeyStore.search(key)
    if not user:
        abort(401)

    return NotImplemented()