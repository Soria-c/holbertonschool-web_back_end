#!/usr/bin/env python3
"""Pymongo"""


def insert_school(mongo_collection, **kwargs):
    """Function that inserts a new document in a collection based on kwargs"""
    return mongo_collection.insert(kwargs)
