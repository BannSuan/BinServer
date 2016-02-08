# -*- coding: utf-8 -*-

# Title: User imprement
# Author: Pongsakorn Sommalai
# Descripter: User imprement
# Date 09/02/2016

from protocal import protocal

class user(protocal):
	def get(self, request):
		return "eiei"

	def post(self, request):
		return "eiei post"

	def put(self, request):
		return "eiei put"
