#!/usr/bin/env python3
"""Session auth module"""

import os
from typing import TypeVar
from api.v1.auth import auth
from models.user import User
import uuid

from models.user_session import UserSession


class SessionAuth(auth.Auth):
    """Session auth class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session id and returns it"""
        if (not user_id or not isinstance(user_id, str)):
            return None
        session_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns user id for a given session id"""
        if (not session_id or not isinstance(session_id, str)):
            return None
        return SessionAuth.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the current User object"""
        session_id = request.cookies.get(os.getenv("SESSION_NAME"))
        return User.get(self.user_id_for_session_id(session_id))

    def destroy_session(self, request=None):
        if not request:
            return False
        session_id = self.session_cookie(request)
        if not session_id:
            return False
        del SessionAuth.user_id_by_session_id[session_id]
        return True
