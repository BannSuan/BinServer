#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from config import Config
# For dev
from flask.ext.script import Manager, Server

from user import user_api 
from room import room_api 
from message import message_api 
from auth import auth_api 

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify(msg="Hello World!")
@app.errorhandler(404)
def not_found(error):
    return jsonify(msg="Find something?")

app.register_blueprint( user_api )
app.register_blueprint( room_api )
app.register_blueprint( message_api )
app.register_blueprint( auth_api )

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