#!/usr/bin/env python3
"""Define filter_datum function"""


from typing import List
import logging
import re
import os

def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Return the log message obfuscated"""
    return re.sub(r"(\w+)=([a-zA-Z0-9@\.\-\(\)\ \:\^\<\>\~\$\%\@\?\!\/]*)",
                  lambda x: x.group(1) + "=" + redaction
                  if x.group(1) in fields else x.group(0), message)
