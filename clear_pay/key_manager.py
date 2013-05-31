# -*- coding: utf-8 -*-
import time
import uuid

from werkzeug.security import (generate_password_hash, check_password_hash)
import pymongo

mong = pymongo.MongoClient()
db = mong.clear_pay

def exists(key):
    return db.api_keys.find({"key": key}).count() > 0

def email_used(email):
    return db.api_keys.find({"email": email}).count() > 0

def delete(value, field="email"):
    """ The field can be set to 'email', 'key', or whatever
        unique identifier is attached to a given person.
    """
    rem = db.api_keys.remove({field: value}, True)
    return rem['n'] == 1

def find(email):
    if not email_used(email):
        return False
    return db.api_keys.find_one({"email": email})

def add(email, password, key=None, created=None, state=None):
    if email_used(email):
        return False
    if key is None:
        # Guaranteed randomness, or my money back.
        key = str(uuid.uuid4())
        while exists(key):
            key = str(uuid.uuid4())
    if created is None:
        created = int(time.time())
    if state is None:
        state = "active"
    pw_hash = generate_password_hash(password) if password else ''
    data = {
        "email": email,
        "password": pw_hash,
        "key": key,
        "created": created,
        "state": state
    }
    if db.api_keys.insert(data):
        return key
    return False

def recoverable(email, password):
    if not email_used(email):
        return False
    row = db.api_keys.find_one({"email": email})
    if len(row['password']) == 0:
        # No password given.
        return False
    return check_password_hash(row['password'], password)
