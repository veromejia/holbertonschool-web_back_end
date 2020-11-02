#!/usr/bin/env python3
"""Define filter_datum function"""


from typing import List
import logging
import re
import os
import csv
import mysql.connector

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Return the log message obfuscated"""
    return re.sub(r"(\w+)=([a-zA-Z0-9@\.\-\(\)\ \:\^\<\>\~\$\%\@\?\!\/]*)",
                  lambda x: x.group(1) + "=" + redaction
                  if x.group(1) in fields else x.group(0), message)


def get_logger() -> logging.Logger:
    """Return a logger object"""
    log = logging.getLogger('user_data')
    log.setLevel(logging.INFO)
    log.propagate = False
    sh = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    sh.setFormatter(formatter)
    log.addHandler(sh)
    return log


def get_db() -> mysql.connector.connection.MySQLConnection:
    """"Return connector to database"""
    connector = mysql.connector.connect(
        user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        host=os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=os.getenv('PERSONAL_DATA_DB_NAME'))
    return connector


def main() -> None:
    ''' Log user info from database. '''
    db = get_db()
    cursor = db.cursor()
    query = ('SELECT * FROM users')
    cursor.execute(query)

    attr = 'name={:s}; email={:s}; phone={:s}; ssn={:s}; password={:s};\
                ip={:s}; last_login={}; user_agent={:s};'
    for (name, email, phone, ssn, password, ip, last_login, user_agent) \
            in cursor:
        print(attr.format(
            name, email, phone, ssn, password, ip, last_login, user_agent))
    cursor.close()
    db.close()


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


if __name__ == '__main__':
    main()
