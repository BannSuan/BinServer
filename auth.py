#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
    * Authentication API
    Login:
        http: POST /auth 
        args: username, password
    Register:
        http: PUT /auth
        args: username, password, email
    Logout:
        http: GET /auth/logout
"""

from flask import Blueprint, abort, request, session, jsonify
from db import DB, GetHash, KeyStore, GenerateKey, validPassword
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
                        })
        if not user or not validPasssword(password, user['password']):
            return jsonify(status="ok", message="Authenticate failed", data={}), 401

        key = GenerateKey()
        KeyStore.save(key, user)
        return jsonify(status="ok", message="Welcome back, {0}.".format(username), data={"key":key, "user":user})

    if request.method == 'PUT': # Register
        username = request.form["username"]
        password = GetHash( request.form["password"] )
        fullname = request.form["fullname"]
        email = request.form["email"]
        user = auth_db.find_one({
                            "username":username, 
                        })
        if user:
            return jsonify(status="fail", message="Username {0} already exist".format(username), data={})
        result = auth_db.insert_one({"username":username, "password":password})
        if not result:
            return jsonify(status="fail", data="DB Fail"), 500
        return jsonify(status="ok", message="Welcome {0}".format(username), data={})

@auth_api.route('/auth/logout', methods=['GET'])
def logout():
    key = request.headers.get('key')
    user = KeyStore.search(key)
    if user:
        KeyStore.delete(key)
        return jsonify(status="ok", message="See ya :D", data={})
    return jsonify(status="fail", message="not authenticated", data={})