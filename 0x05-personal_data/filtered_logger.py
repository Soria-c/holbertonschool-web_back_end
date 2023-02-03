#!/usr/bin/env python3
"""obfuscator"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns message string with the required fields obfuscated"""
    os = message
    for i in fields:
        os = re.sub(rf"{i}=(.+?)(?={separator})", f"{i}={redaction}", os)
    return os
