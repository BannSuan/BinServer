#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from flask import Blueprint, abort, request, session, jsonify
from db import DB, GetUserFromToken

room_db = DB['rooms']
room_api = Blueprint('room_api', __name__)

@room_api.route('/room/<token>', methods=['GET', 'POST'])
def room(token):
    user = GetUserFromToken(token)
    if not user:
        abort(400)
    return NotImplemented()