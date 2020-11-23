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
    """DB class"""

    def __init__(self):
        """initialization"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
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

    def find_user_by(self, **user_table) -> User:
        """Return matching User instance"""
        if not user_table:
            raise InvalidRequestError

        fields = ['id', 'email', 'hashed_password',
                  'session_id', 'reset_token']

        for arg in user_table:
            if arg not in fields:
                raise InvalidRequestError
        user = self._session.query(User).filter_by(**user_table).first()
        if not user:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **user_table) -> None:
        """Update user information"""
        user = self.find_user_by(id=user_id)

        fields = ['id', 'email', 'hashed_password',
                  'session_id', 'reset_token']
        for key, value in user_table.items():
            if key not in fields:
                raise ValueError
            setattr(user, key, value)
        self._session.commit()
