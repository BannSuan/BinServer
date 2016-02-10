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
    return jsonify(**Config['ERROR'][0]), 200

@app.errorhandler(401)
def e401(error):
    return jsonify(**Config['ERROR'][401]), 401

@app.errorhandler(404)
def e404(error):
    return jsonify(**Config['ERROR'][404]), 404

@app.errorhandler(405)
def e405(error):
    return jsonify(**Config['ERROR'][405]), 405

@app.errorhandler(410)
def e410(error):
    return jsonify(**Config['ERROR'][410]), 410

@app.errorhandler(500)
def e500(error):
    return jsonify(**Config['ERROR'][500]), 500


app.register_blueprint( user.user_api )
app.register_blueprint( room.room_api )
app.register_blueprint( message.message_api )
app.register_blueprint( auth.auth_api )


# Turn on debugger by default and reloader
manager = Manager(app)
manager.add_command("runserver", Server(
    use_debugger = Config['DEBUG'],
    use_reloader = Config['DEBUG'],
    host = Config['HOST'],
    port = (Config['PORT'] if not Config['DEBUG'] else Config['DEBUG_PORT']) ),
)

if __name__ == "__main__":
    manager.run()
