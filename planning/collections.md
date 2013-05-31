api_keys
========
Holds information on the API keys given out to developers.

+ `email` - the email address given at signup
+ `password` - hashed password (optional), used for recovery of password
    + Should just be empty if they don't give one. No recovery for you, buddy.
+ `key` - the given api key
+ `created` - time.time() of creation
+ `state` - the state of the key, `active`, `banned`, or whatever stupid crap I deem needed.

addresses
=========
Holds information on the addresses registered with the Bloocoin <strike>Fuhrer</strike> server.

+ `created` - time.time() of registration
+ `addr` - the address - should we prefix it with something? Maybe.
+ `pwd` - the password/key affiliated with the address.
+ `state` - `waiting`, `inactive`, _other_?
    + `waiting` represents the address is still being used in a transaction.
    + `inactive` means the address isn't in use, and can be reused, if required.
