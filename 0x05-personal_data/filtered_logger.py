#!/usr/bin/env python3
"""obfuscator"""
from cgitb import handler
from typing import List
import re
import logging

PII_FIELDS = ("Phone", "Email", "Ip", "Password", "Ssn")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns message string with the required fields obfuscated"""
    os = message
    for i in fields:
        os = re.sub(rf"{i}=(.+?)(?={separator})", f"{i}={redaction}", os)
    return os


def get_logger() -> logging.Logger:
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(logging.StreamHandler())
    return logger


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """returns formated string"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)