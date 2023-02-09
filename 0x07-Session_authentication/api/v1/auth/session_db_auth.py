#!/usr/bin/env python3
"""Session auth module"""

from api.v1.auth import session_exp_auth
from models.user_session import UserSession
import os


class SessionDBAuth(session_exp_auth.SessionExpAuth):
    """Session db auth class"""

    def create_session(self, user_id=None):
        """Overload of create session"""
        session_id = super().create_session(user_id)
        session = UserSession(user_id=user_id, session_id=session_id)
        session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Overload of user_id_for_session_id"""
        return UserSession.search({"session_id": session_id})[0].user_id

    def destroy_session(self, request=None):
        """Overload of destroy session"""
        self.user_id_for_session_id(request.cookies
                                    .get(os.getenv("SESSION_NAME"))).remove()
