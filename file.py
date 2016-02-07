#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
    * File Upload API

"""

from flask import Blueprint, abort, request, session, jsonify
from db import DB, KeyStore

file_db = DB['files']
file_api = Blueprint('file_api', __name__)

@file_api.route('/file', methods=['GET', 'POST'])
@file_api.route('/file/<id>', methods=['GET'])
def file():
    key = request.headers.get('x-key')
    user = KeyStore.search(key)
    if not user:
        return jsonify(status="fail", msg="UNAUTHORIZED", data={}), 401

    return NotImplemented()