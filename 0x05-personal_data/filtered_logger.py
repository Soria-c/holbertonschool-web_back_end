#!/usr/bin/env python3
"""obfuscator"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns message string with the required fields obfuscated"""
    os = message
    for i in fields:
        os = re.sub(re.search(rf"{i}=(.+?)(?={separator})", os)
                    .group(1), redaction, os, 1)
    return os
