from app.libs.redprint import Redprint

api = Redprint('book')

@api('/v1/user/get')
def get_user():
    pass