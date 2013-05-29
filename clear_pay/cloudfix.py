# -*- coding: utf-8 -*-


class CloudFix(object):
    """ Fixes the REMOTE_ADDR given if the app is run
        behind CloudFlare w/ nginx setting CF-Connecting-IP.
    """

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        connecting_ip = environ.get('HTTP_CF_CONNECTING_IP', '')
        if host:
            environ['REMOTE_ADDR'] = connecting_ip
        return self.app(environ, start_response)
# app.wsgi_app = CustomProxyFix(app.wsgi_app)
