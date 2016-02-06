#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from flask import Blueprint, abort, request, session, jsonify
from db import DB, GetUserFromToken

user_db = DB['users']
user_api = Blueprint('user_api', __name__)

@user_api.route('/user/<token>', methods=['GET', 'POST'])
def user(token):
    user = GetUserFromToken(token)
    if not user:
        abort(400)
    return NotImplemented()