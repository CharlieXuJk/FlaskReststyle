class APIException(HTTPException):
    code = 500
    msg = 'sry, there is a mistake'
    error_code = 999

    def __init__(self, msg=None, code=None, error_code=None):


    def get_body(self, environ=None):
        body = dict(


            request='POST V1/client/register'
        )

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]


    @staticmethod
    def get_url_no_param():
        full_path = str()



