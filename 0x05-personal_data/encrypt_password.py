#!/usr/bin/env python3
"""define hash_password function"""


import bcrypt


def hash_password(password: str) -> bytes:
    """Return encrypted password"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(str.encode(password), salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check validity of password"""
    if hashed_password and password:
        return bcrypt.checkpw(str.encode(password), hashed_password)
