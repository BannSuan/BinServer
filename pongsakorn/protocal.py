# -*- coding: utf-8 -*-

# Title: Protocal for impementation
# Author: Pongsakorn Sommalai
# Descripter: Protocal class
# Date 09/02/2016

from flask import jsonify
from config import Config

class protocal:
	def failkey(self):
		return jsonify(status="fail", msg=Config["error"][401], data={}), 401

	def get(self, request):
		return jsonify(status="fail", msg=Config["error"][410], data={}), 410

	def post(self, request):
		return jsonify(status="fail", msg=Config["error"][410], data={}), 410

	def put(self, request):
		return jsonify(status="fail", msg=Config["error"][410], data={}), 410

	def delete(self, request):
		return jsonify(status="fail", msg=Config["error"][410], data={}), 410

	def other(self, request):
		return jsonify(status="fail", msg=Config["error"][410], data={}), 410
