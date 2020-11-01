#!/usr/bin/env python3
"""Define filter_datum function"""


from typing import List
import logging
import re
import os


PII_FIELDS = ("name", "email", "phone", "ssn", "ip")


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Return the log message obfuscated"""
    return re.sub(r"(\w+)=([a-zA-Z0-9@\.\-\(\)\ \:\^\<\>\~\$\%\@\?\!\/]*)",
                  lambda x: x.group(1) + "=" + redaction
                  if x.group(1) in fields else x.group(0), message)


def get_logger() -> logging.Logger:
    """ Return a logger object """
    log = logging.getLogger("user_data")
    log.setLevel(logging.INFO)
    log.propagate = False
    sh = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    sh.setFormatter(formatter)
    log.addHandler(sh)
    return log


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """initalization"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """method to filter values in incoming log records
        using filter_datum"""
        return filter_datum(self.fields, self.REDACTION,
                            super(RedactingFormatter, self).format(record),
                            self.SEPARATOR)
