#!/usr/bin/env python3
"""
Basic Auth module
"""
from api.v1.auth import auth
from models.user import User
import base64
from typing import Tuple, TypeVar


class BasicAuth(auth.Auth):
    """Basic Auth class"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Return the base64 string from the auth header"""
        if (not authorization_header or
                not isinstance(authorization_header, str)):
            return None
        auth_str = authorization_header.split(" ")
        return auth_str[1] if (auth_str[0] == "Basic") else None

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """Decodes the base64 string"""
        if (not base64_authorization_header or
                not isinstance(base64_authorization_header, str)):
            return None
        try:
            return base64.b64decode(base64_authorization_header).\
                            decode("utf-8")
        except Exception as e:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> Tuple[str, str]:
        """Returns user credentials"""
        if (not decoded_base64_authorization_header or
                not isinstance(decoded_base64_authorization_header, str)):
            return (None, None)
        credentials = decoded_base64_authorization_header.split(":", 1)
        return (None, None) if (len(credentials) == 1)\
            else (credentials[0], credentials[1])

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """returns User instance based on his email and password."""
        if (not user_email or not isinstance(user_email, str)):
            return None
        if (not user_pwd or not isinstance(user_pwd, str)):
            return None
        users = User.search({"email": user_email})
        if (not users):
            return None
        for u in users:
            if u.is_valid_password(user_pwd):
                return u
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns current user"""
        auth_header = self.authorization_header(request)
        if (not auth_header):
            return None
        h_value = self.extract_base64_authorization_header(auth_header)
        decoded = self.decode_base64_authorization_header(h_value)
        credetials = self.extract_user_credentials(decoded)
        user_obj = self.user_object_from_credentials(*credetials)
        return user_obj
