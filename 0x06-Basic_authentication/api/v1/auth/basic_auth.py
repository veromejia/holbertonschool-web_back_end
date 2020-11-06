#!/usr/bin/env python3
""" Basic authentication module
"""

from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """BasicAuth class"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header
        for a Basic Authentication"""
        if authorization_header is None or type(
                authorization_header) is not str:
            return None
        return authorization_header[6:] \
            if authorization_header.startswith('Basic ') else None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """returns the decoded value of a Base64 string"""
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            return None

        try:
            header = base64_authorization_header.encode('utf-8')
            header = b64decode(header)
            header = header.decode('utf-8')
            return header
        except BaseException:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """returns the user email and passw from the Base64 decoded value."""
        if decoded_base64_authorization_header is None \
                or not isinstance(decoded_base64_authorization_header, str) \
                or ':' not in decoded_base64_authorization_header:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on his email and password"""
        if user_email is None or user_pwd is None or not isinstance(
                user_email, str) or not isinstance(user_pwd, str):
            return None

        user_search = User.search({'email': user_email})

        for user in user_search:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """authorization for user"""
        auth_header = self.authorization_header(request)
        if not auth_header:
            return None
        auth_header = self.extract_base64_authorization_header(auth_header)
        auth_header = self.decode_base64_authorization_header(auth_header)
        if not auth_header:
            return None
        user = self.extract_user_credentials(auth_header)

        return self.user_object_from_credentials(user[0], user[1])
