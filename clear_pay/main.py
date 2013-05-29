# -*- coding: utf-8 -*-
import gevent
import gevent.monkey
gevent.monkey.patch_all()

import sys
import json

from flask import (Flask, render_template, request, session, url_for,
                   redirect, flash)
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, IntegerField
from gevent.pywsgi import WSGIServer
from cloudfix import CloudFix


app = Flask(__name__)

@app.route("/")
def index():
    return "Hnnnng!"
