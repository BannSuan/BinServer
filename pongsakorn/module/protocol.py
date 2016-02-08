# -*- coding: utf-8 -*-

# Title: Protocal for impementation
# Author: Pongsakorn Sommalai
# Descripter: Protocal class
# Date 09/02/2016

from flask import jsonify
from config import Config

class protocol:

	def error(self, code):
		return jsonify(status="fail", msg=Config["error"][code], data={}), code

	def failkey(self):
		return self.error(401)

	def get(self, request):
		return self.error(410)

	def post(self, request):
		return self.error(410)

	def put(self, request):
		return self.error(410)

	def delete(self, request):
		return self.error(410)

	def other(self, request):
		return self.error(410)
