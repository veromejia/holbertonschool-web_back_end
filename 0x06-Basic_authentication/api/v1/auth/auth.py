#!/usr/bin/env python3
""" Define Auth class """


from flask import request
from typing import List, TypeVar


class Auth:
    """Auth Class that handle public methods"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if path requires authentication"""
        if path is None or excluded_paths is None:
            return True

        if path[-1] is not '/':
            path += '/'

        return False if path in excluded_paths else True

    def authorization_header(self, request=None) -> str:
        """Check if request is authorized"""

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return current user  """
