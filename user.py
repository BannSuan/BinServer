#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
    * User API

"""

from flask import Blueprint, abort, request, session, jsonify
from db import DB, KeyStore

user_db = DB['users']
user_api = Blueprint('user_api', __name__)

@user_api.route('/user', methods=['GET', 'POST'])
def user():
    key = request.headers.get('x-key')
    user = KeyStore.search(key)
    if not user:
        return jsonify(status="fail", msg="UNAUTHORIZED", data={}), 401

    return NotImplemented()