#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from flask import Blueprint, abort, request, session, jsonify
from db import DB, GetUserFromToken

message_db = DB['messages']
message_api = Blueprint('message_api', __name__)

@message_api.route('/message/<token>', methods=['GET', 'POST'])
def message(token):
    user = GetUserFromToken(token)
    if not user:
        abort(400)
    return NotImplemented()