#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
    * User API

"""

from flask import Blueprint, abort, request, session, jsonify
from db import KeyStore, GenerateKey
import model.users

user_api = Blueprint('user_api', __name__)

@user_api.route('/user', methods=['GET', 'POST', 'PUT'])
@user_api.route('/user/<uid>', methods=['GET'])
def user():
    key = request.headers.get('x-key')
    user = KeyStore.search(key)

    if uid is not None:
        if not user:
            abort(401)

        if uid=="me":
            uid = user["_id"]

        res = model.users.get(uid)
        return jsonify(status="ok", message="", data=res)

    if request.method == 'GET':
        if not user:
            abort(401)

        search = request.args.get("search", "")
        skip = request.args.get("skip", 0)
        limit = request.args.get("limit", 10)

        res = model.users.search(search, skip=skip, limit=limit)

        return jsonify(status="ok", message="", data=res)

    elif request.method == 'POST':
        token = request.form["token"]
        user = model.users.login(token)

        if user:
            key = GenerateKey()
            KeyStore.save(key, user)
            user["key"] = key

            return jsonify(status="ok", message="", data=user)
        else:
            model.users.add(token)
            return jsonify(status="ok", message="news", data={})

    elif request.method == 'PUT':
        token = request.form["token"]
        name = request.form["name"]
        fullname = request.form["fullname"]
        image = request.form["image"]

        if model.users.update(token, name, fullname, image):
            return jsonify(status="ok", message="", data={})
        else:
            abort(404)
