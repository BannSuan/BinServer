#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
    * User API

"""

from flask import Blueprint, abort, request, session, jsonify
from db import KeyStore

user_api = Blueprint('user_api', __name__)

@user_api.route('/user', methods=['GET', 'POST', 'PUT'])
def user():
    key = request.headers.get('x-key')
    user = KeyStore.search(key)

    if request.method == 'GET':
        if not user:
            abort(401)

        return jsonify(status="ok", message="", data=[])

    elif request.method == 'POST':
        token = request.form.args["token"]
