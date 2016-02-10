#!/usr/bin/env python2
# -*- coding: utf-8 -*-

Config = {
    'DEBUG': True,
    'DEBUG_PORT': 5000,
    # Server
    'HOST': "0.0.0.0",
    'PORT': 8888,

    # Hash salt
    'SALT': "adasdasdalknaglnalrgnaoje;rgnjlearngnae",

    # DB name
    'DATABASE': "testBinServer",

    # Google API
    "GOOGLE": {
        "ID": "125904001864-03ujaq1gmejogtpfcpl05btsnjboce5r.apps.googleusercontent.com",
        "SECRET": "eHXp8y0acdqFOuE0G24CYS65"
    },

    # Upload
    'UPLOAD_FOLDER': 'uploads/',
    'ALLOWED_EXTENSIONS': set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']),

    # Error Message
    'ERROR': {
        0: {'status':'ok', 'message':"HI! Nice to meet you. :D"},
        400: {'status':'fail', 'message':"BAD REQUEST"},
        401: {'status':'fail', 'message':"UNAUTHORIZED"},
        404: {'status':'fail', 'message':"NOT FOUND"},
        405: {'status':'fail', 'message':"METHOD NOT ALLOWED"},
        500: {'status':'fail', 'message':"Ops! something went wrong."},
    }
}
