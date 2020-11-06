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
        
        wildcards = [p[:-1] for p in excluded_paths if p[-1] == '*']

        for p in wildcards:
            if path.startswith(p):
                return False

        return False if path in excluded_paths else True

    def authorization_header(self, request=None) -> str:
        """Check if request is authorized"""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return current user  """
