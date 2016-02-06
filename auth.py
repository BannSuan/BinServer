#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from flask import Blueprint, abort, request, session, jsonify
from db import DB, GetUserFromToken, GetHash

from config import Config

auth_db = DB['users']
auth_api = Blueprint('auth_api', __name__)

@auth_api.route('/auth', methods=['PUT', 'POST'])
def auth():
    if request.method == 'POST':
        username = request.form["username"]
        password = GetHash( request.form["password"] )
        user = auth_db.find_one({
                            "username":username, 
                            "password":password
                        })
        if not user:
            return jsonify(msg="Access Denied"), 401
        token = 123
        return jsonify(token=token)
    if request.method == 'PUT':
        # Register
        pass