#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
    * File Upload API

"""

from flask import Blueprint, abort, request, session, jsonify
from db import DB, KeyStore