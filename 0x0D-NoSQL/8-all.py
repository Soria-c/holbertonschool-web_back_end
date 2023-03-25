#!/usr/bin/env python3
"""Pymongo"""


def list_all(mongo_collection):
    """Function that lists all documents in a collection"""
    return mongo_collection.find()
