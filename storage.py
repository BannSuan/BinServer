#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
    * File Upload API

"""

from flask import Blueprint, abort, request, session, jsonify, send_from_directory, url_for
from werkzeug import secure_filename
from db import DB, KeyStore
import os

storage_db = DB['files']
storage_api = Blueprint('storage_api', __name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in Config['ALLOWED_EXTENSIONS']

@storage_api.route('/storage', methods=['POST'])
@storage_api.route('/storage/<file_id>', methods=['GET'])
def storage(file_id=None):
    key = request.headers.get('x-key')
    user = KeyStore.search(key)
    if not user:
        abort(401)

    if request.method is 'POST':
        file = request.files['file']
        room = request.form['room']
        if file and allowed_file(file.filename):
            # secure filename
            filename = secure_filename(file.filename)
            # get id from document id
            ret = file_db.insert_one({"filename": filename, "room":room})
            file_id = ret['_id']
            # save file
            file.save(os.path.join(Config['UPLOAD_FOLDER'], filename))
            return jsonify(status="ok", message="Yippee!", data={'file_id':fileid,})
        return jsonify(status="fail", message="EXTENSION NOT AllOWED ")

    if request.method is 'GET':
        if file_id is not None:
            file_name = ''
            return send_from_directory(Config['UPLOAD_FOLDER'], file_id)
        return jsonify(status="fail", message="FILE NOT FOUND")


