# -*- coding: utf-8 -*-
import gevent
import gevent.monkey
gevent.monkey.patch_all()
from gevent.queue import Queue

import sys
import json
import threading

from flask import (Flask, render_template, request, session, url_for,
                   redirect, flash, abort)
from flask.ext.wtf import Form, validators
from wtforms import (TextField, PasswordField, IntegerField,
                     BooleanField)
from gevent.pywsgi import WSGIServer
from recaptcha.client import captcha


from cloudfix import CloudFix
import key_manager


class RegisterForm(Form):
    email = TextField("e-mail (required)", [validators.Required()])
    password = PasswordField("password (optional)")
    recover = BooleanField("recover lost key")


# Monkey-patch for dev testing.
# (this just points to my developer bloocoin-server)
#import blcpy
#blcpy._Transaction._server = ("monkey.dev", 3122)

app = Flask(__name__)
config = {}
with open('config.json', 'rb') as f:
    config = json.load(f)
    app.config.update(**config)
    app.config['SECRET_KEY'] = str(config['SECRET_KEY'])
    if config['cloudflare'] is True:
        app.wsgi_app = CloudFix(app.wsgi_app)

#jobs = Queue()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/tos")
def tos():
    return render_template("tos.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    kw = {
        "form": form,
        "recaptcha_public_key": config['recaptcha_public']
    }
    # Sort of a filthy hack, but you know..
    render = lambda: render_template("register.html", **kw)
    if form.validate_on_submit():
        response = captcha.submit(
            request.form['recaptcha_challenge_field'],
            request.form['recaptcha_response_field'],
            config['recaptcha_private'],
            request.remote_addr
        )
        if not response.is_valid:
            flash("The captcha typed was incorrect.", "error")
            return render()

        if form.recover.data:
            if not key_manager.email_used(form.email.data):
                flash("Sorry, that email isn't in use.", "error")
                return render()
            if not key_manager.recoverable(form.email.data, form.password.data):
                flash("Sorry, the password given was incorrect.", "error")
                return render()
            kw['recover_key'] = key_manager.find(form.email.data)['key']
            return render()

        if key_manager.email_used(form.email.data):
            flash("Sorry, that email is already in use. Did you mean to recover?", "error")
            return render()
        key = key_manager.add(form.email.data, form.password.data)
        if not key:
            flash("Something went wrong generating an API key, please try again.", "error")
            return render()
        flash("Successfully generated an API key, here you go!", "success")
        kw['recover_key'] = key
    return render()


@app.route("/pay", methods=["POST"])
def api_pay():
    # handle step 2 and 6a.
    abort(403)

# Purely for debugging reasons, use gunicorn instead!
if __name__ == "__main__" and "--wsgi-serve" in sys.argv:
    serv = WSGIServer(('127.0.0.1', 3125), app)
    serv.serve_forever()
