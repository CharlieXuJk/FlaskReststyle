from flask import Blueprint

from app.libs.redprint import Redprint

api = Redprint('user')


@api.route('/get')
def get_user():
    pass


@api.route('/create')
def create_user():
    pass