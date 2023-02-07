#!/usr/bin/env python3
"""
Auth module
"""

from typing import List, TypeVar
from flask import request


class Auth():
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if @path needs authentication"""
        if (not path or not excluded_paths):
            return True
        path = path if path[-1] == '/' else path + '/'
        for paths in excluded_paths:
            if paths.endswith('*'):
                if path.startswith(paths[:-1]):
                    return False
            elif path == paths:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Returns the value of Authorization header"""
        if (not request):
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the current User object"""
        return None
