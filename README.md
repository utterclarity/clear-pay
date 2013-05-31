clear-pay
=========
An IPN-like style payment middle-man for BlooCoin.  
Called __Clear Pay__, but sometimes referred to simply as __Pay__.

# THIS PROJECT IS UNDER MAJOR DEVELOPMENT!
We're still working out the kinks in our planning before we begin development.  
You're free to run this, but be aware it might be lacking full implementations, or be riddled with bugs and developer testing code.

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
    "cloudflare": false,
    "recaptcha_public": "your_recaptcha_public_key",
    "recaptcha_private": "your_recaptcha_private_key"
}
```


## Expected dependencies
You can see the dependencies in the `requirements.txt` file. Install with `pip -r requirements.txt install`  
I'm not sure if the line for `blc.py` worked (`-e git+git://whatever`), so that might fail spectacularly.

## Explanation
Here's a somewhat cryptic explanation of what is planned for Pay: (this is `r1`, and subject to major change)

![cryptic explanation](https://raw.github.com/utterclarity/clear-pay/master/planning/pay_plan_r1.png)
