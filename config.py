#!/usr/bin/env python2
# -*- coding: utf-8 -*-

Config = {
    'DEBUG': True,
    # Server
    'HOST': "0.0.0.0",
    'PORT': 5000,

    # Hash salt
    'SALT': "adasdasdalknaglnalrgnaoje;rgnjlearngnae",

    # DB name
    'DATABASE': "testBinServer",

    "GOOGLE": {
        "id": "125904001864-03ujaq1gmejogtpfcpl05btsnjboce5r.apps.googleusercontent.com",
        "secret": "eHXp8y0acdqFOuE0G24CYS65"
    },

    'UPLOAD_FOLDER': 'uploads/',
    'ALLOWED_EXTENSIONS': set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']),

    "ERROR": {
        401: "UNAUTHORIZED",
        410: "METHOD NOT FOUND"
    }
}
