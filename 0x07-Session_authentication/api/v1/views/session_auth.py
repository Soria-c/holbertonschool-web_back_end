#!/usr/bin/env python3
""" Module of Session auth views
"""

from api.v1.views import app_views
from flask import request, jsonify, abort
from api.v1.app import auth
import os
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session_login():
    """Auth session login endpoint"""
    email = request.form.get("email")
    password = request.form.get("password")
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400
    try:
        users = User.search({"email": email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404
    if not users:
        return jsonify({"error": "no user found for this email"}), 404
    for i in users:
        user = i.is_valid_password(password)
        if user:
            from api.v1.app import auth
            session = auth.create_session(i.id)
            resp = jsonify(i.to_json())
            resp.set_cookie(os.getenv("SESSION_NAME"), session)
            return resp

    return jsonify({"error": "wrong password"}), 401


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def session_logout():
    """Logout function"""
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
