#!/usr/bin/env python3
"""Session auth module"""

from datetime import datetime, timedelta
import os
from api.v1.auth import session_auth


class SessionExpAuth(session_auth.SessionAuth):
    """Session Exp auth class"""

    def __init__(self):
        """Constructor"""
        self.session_duration = int(os.getenv("SESSION_DURATION", 0))

    def create_session(self, user_id=None):
        """Overload with exp time"""
        session = super().create_session(user_id)
        if not session:
            return None
        self.user_id_by_session_id[session] = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        return session

    def user_id_for_session_id(self, session_id=None):
        """Returns user id for a given session id"""
        session_dict = self.user_id_by_session_id.get(session_id)
        if (not session_id or not session_dict):
            return None
        if self.session_duration <= 0:
            return session_dict.get("user_id")
        if not(session_dict.get("created_at")):
            return None
        if (timedelta(minutes=self.session_duration)
                + session_dict["created_at"] < datetime.now()):
            return None
        return session_dict.get("user_id")
