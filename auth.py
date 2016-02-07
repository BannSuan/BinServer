#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from flask import Blueprint, abort, request, session, jsonify
from db import DB, GetUserFromToken, GetHash

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
        token = 123 # Generate new Token or some OAuth Spec
        result auth_db.update_one({"username":username},{
                "$set": {
                    "token": token
                },
                "$currentDate": {"lastModified": True}
            })
        if result.modified_count != 1:
            return jsonify(msg="Try Again Later"), 500
        return jsonify(token=token)
        
    if request.method == 'PUT': # Register
        username = request.form["username"]
        password = GetHash( request.form["password"] )
        result = auth_db.insert_one({"username":username, "password":password})
        if not result:
            return jsonify(msg="Try Again Later"), 500
        return jsonify(msg="OK")
        