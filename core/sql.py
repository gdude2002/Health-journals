__author__ = 'Gareth Coles'
from bottle.ext import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Setup(object):

    engine = None
    plugin = None

    def __init__(self, app, db_url):
        self.engine = create_engine(db_url, echo=True)

        self.plugin = sqlalchemy.Plugin(
            self.engine,
            Base.metadata,
            keyword='db',
            create=True,
            commit=True,
            use_kwargs=False
        )

        app.install(self.plugin)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('users_id_seq'), primary_key=True)
    username = Column(String(255))
    password = Column(String(255))
    salt = Column(String(255))

    def __init__(self, username, password, salt):
        self.username = username
        self.password = password
        self.salt = salt

    def __repr__(self):
        return "<User (%s, %s)>" % (self.id, self.username)
