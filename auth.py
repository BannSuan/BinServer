#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from flask import Blueprint, abort, request, session, jsonify
from db import DB, GetHash, KeyStore, GenerateKey

from config import Config

auth_db = DB['users']
auth_api = Blueprint('auth_api', __name__)

@auth_api.route('/auth', methods=['PUT', 'POST'])
def auth():
    if request.method == 'POST': # Login
        username = request.form["username"]
        password = GetHash( request.form["password"] )
        user = auth_db.find_one({
                            "username":username, 
                            "password":password
                        })
        if not user:
            return jsonify(msg="Access Denied"), 401
        key = GenerateKey()
        KeyStore.save(key, user)
        if result.modified_count != 1:
            return jsonify(msg="Try Again Later"), 500
        return jsonify(key=key)

    if request.method == 'PUT': # Register
        username = request.form["username"]
        password = GetHash( request.form["password"] )
        result = auth_db.insert_one({"username":username, "password":password})
        if not result:
            return jsonify(msg="Try Again Later"), 500
        return jsonify(msg="OK")
        