#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
    * File Upload API

"""

from flask import Blueprint, abort, request, session, jsonify, send_from_directory, url_for
from werkzeug import secure_filename
from db import DB, KeyStore
import os

file_db = DB['files']
file_api = Blueprint('file_api', __name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in Config['ALLOWED_EXTENSIONS']

@file_api.route('/file', methods=['POST'])
@file_api.route('/file/<file_id>', methods=['GET'])
def file(file_id=None):
    key = request.headers.get('x-key')
    user = KeyStore.search(key)
    if not user:
        abort(401)

    if request.method == 'POST':
        file = request.files['file']
        room = request.form['room']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(Config['UPLOAD_FOLDER'], filename))
            fileid = file_db.insert_one({"filename": filename, "room":room})
            return jsonify(status="ok", message="Yippee!", data={fileid,})
        return jsonify(status="fail", msg="Not Allowed Extension", data={})

    if request.method == 'GET':
        if not file_id:
            return send_from_directory(Config['UPLOAD_FOLDER'], file_id)
        return jsonify(status="fail", message="File Not Found", data={})


