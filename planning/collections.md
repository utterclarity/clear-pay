api_keys
========

+ `created` - time.time() of creation
+ `key` - the given api key
+ `email` - the email address given at signup
+ `password` - hashed password (optional), used for recovery of password
    + Should just be empty if they don't give one. No recovery for you, buddy.
+ `state` - the state of the key, `active`, `banned`, or whatever stupid crap I deem needed.
