# -*- coding: utf-8 -*-

# Title: API to use pongsakorn library
# Author: Pongsakorn Sommalai
# Descripter: API to use pongsakorn library
# Date 09/02/2016

from module.protocol import protocol
from mException import MethodException, BuildException
from module import user

USER = 0

def build(t):
	global USER

	if (t==USER):
		return user.main()
	else:
		raise BuildException("type not found")


def execute(obj, request, user, auth=["GET", "POST", "PUT", "DELETE"]):

	if not isinstance(obj, protocol):
		raise ProtocalException("please extend protocol class")

	if request.method=="GET":
		if "GET" in auth and not user:
			return obj.failkey()

		return obj.get(request)

	elif request.method=="POST":
		if "POST" in auth and not user:
			return obj.failkey()

		return obj.post(request)

	elif request.method=="PUT":
		if "PUT" in auth and not user:
			return obj.failkey()

		return obj.put(request)

	elif request.method=="DELETE":
		if "DELETE" in auth and not user:
			return obj.failkey()

		return obj.delete(request)

	else:
		return obj.other(request)
