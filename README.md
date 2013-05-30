clear-pay
=========
An IPN-like style payment middle-man for BlooCoin.  
Called __Clear Pay__, but sometimes referred to simply as __Pay__.

Running
-------
Pay is best run via gunicorn:  
`gunicorn -w 3 -k gevent -b :3125 -p ~/gunicorn-pay.pid main:app`  
It might be more beneficial to bind to a unix socket (`-b unix:/tmp/gunicorn-pay.sock`), allowing somewhat better pass-through with nginx (explained later).

For more information, check out [other servers](http://flask.pocoo.org/docs/deploying/others/) in the Flask docs.  
Implemented but not setup yet is a CloudFlare proxy header fix (`cloudfix.CloudFix`), in-case you run behind CloudFlare with nginx setting `CF-Connecting-IP` as is suggested.

config.json
-----------
```json
{
    "SECRET_KEY": "__secret__",
    "cloudflare": False
}
```

# THIS PROJECT IS UNDER MAJOR DEVELOPMENT!
We're still working out the kinks in our planning before we begin development.

## Expected dependencies
+ `Python` (2.7.3+)
+ `gevent` (w/ `gunicorn`?)
+ `pysqlw` / `pymongo` (undecided)
+ `blc.py` (from John Smith's [blc.py](https://github.com/jognsmith/blc.py) repo)
+ `Flask`, `Flask-WTF`, `wtforms`

## Explanation
Here's a somewhat cryptic explanation of what is planned for Pay: (this is `r1`, and subject to major change)

![cryptic explanation](https://raw.github.com/utterclarity/clear-pay/master/planning/pay_plan_r1.png)
