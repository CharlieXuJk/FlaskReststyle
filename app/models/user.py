from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash


class User(Base):
    id = Column(Integer, primary_key= True)
    email = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24), unique=True)
    auth = Column(SmallInteger, default=1)
    _password = Column('password', String(100))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def register_by_email(sel):