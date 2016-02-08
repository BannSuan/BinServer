#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
    * User API

"""

from flask import Blueprint, abort, request, session, jsonify
from db import DB, KeyStore
from pongsakorn import factory

user_db = DB['users']
user_api = Blueprint('user_api', __name__)
u = factory.build(factory.USER)

@user_api.route('/user', methods=['GET', 'POST', 'PUT', 'DELETE'])
def user():
    key = request.headers.get('x-key')
    user = KeyStore.search(key)

    return factory.execute(u, request, user, auth=["GET"])
