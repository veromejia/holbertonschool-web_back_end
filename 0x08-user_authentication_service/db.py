#!/usr/bin/env python3
"""
SQLAlchemy model DB
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """ DB class """

    def __init__(self):
        """initialization"""
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Create session if it does not exist and return it"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Create user with given email/password and
        return new User instance"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Return matching User instance"""
        if not kwargs:
            raise InvalidRequestError

        valid_columns = ['id', 'email', 'hashed_password', 'session_id',
                         'reset_token']
        for key in kwargs:
            if key not in valid_columns:
                raise InvalidRequestError

        found_user = self._session.query(User).filter_by(**kwargs).first()
        if found_user is None:
            raise NoResultFound
        return found_user

    def update_user(self, user_id: str, **kwargs) -> None:
        """Update user information"""
        user = self.find_user_by(id=user_id)

        fields = ['id', 'email', 'hashed_password',
                  'session_id', 'reset_token']
        for key, val in kwargs.items():
            if key not in fields:
                raise ValueError
            setattr(user, key, val)

        self._session.commit()
