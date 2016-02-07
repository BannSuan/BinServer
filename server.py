#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from config import Config
# For dev
from flask.ext.script import Manager, Server

import user, room, message, auth
app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify(status="ok", msg="HI! Nice to meet you. :D", data={})

@app.errorhandler(404)
def not_found(error):
    return jsonify(status="fail", msg="What are you looking for?", data={})

@app.errorhandler(500)
def not_found(error):
    return jsonify(status="fail", msg="Ops! something went wrong.", data={})

app.register_blueprint( user.user_api )
app.register_blueprint( room.room_api )
app.register_blueprint( message.message_api )
app.register_blueprint( auth.auth_api )

# Turn on debugger by default and reloader
manager = Manager(app)
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host=Config['host'],
    port=Config['port'])
)

if __name__ == "__main__":
    if Config['DEBUG']:
        manager.run()
    else:
        app.run(host=Config['host'], port=Config['port'])