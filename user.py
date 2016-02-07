#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from flask import Blueprint, abort, request, session, jsonify
from db import DB, KeyStore

user_db = DB['users']
user_api = Blueprint('user_api', __name__)

@user_api.route('/user', methods=['GET', 'POST'])
def user():
    key = request.headers.get('key')
    user = KeyStore.search(key)
    if not user:
        return jsonify(), 401

    return NotImplemented()