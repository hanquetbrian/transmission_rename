from six import string_types, integer_types


class TransmissionError(Exception):
    def __init__(self, message=''):
        Exception.__init__(self)
        self.message = message

    def __str__(self):
        return self.message


class HTTPError(Exception):
    def __init__(self, httpurl=None, httpcode=None, httpmsg=None, httpheaders=None, httpdata=None):
        Exception.__init__(self)
        self.url = ''
        self.code = 600
        self.message = ''
        self.headers = {}
        self.data = ''
        if isinstance(httpurl, string_types):
            self.url = httpurl
        if isinstance(httpcode, integer_types):
            self.code = httpcode
        if isinstance(httpmsg, string_types):
            self.message = httpmsg
        if isinstance(httpheaders, dict):
            self.headers = httpheaders
        if isinstance(httpdata, string_types):
            self.data = httpdata

    def __str__(self):
        return 'HTTPHandlerError %d: %s' % (self.code, self.message)
