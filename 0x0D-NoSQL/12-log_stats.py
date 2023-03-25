#!/usr/bin/env python3
from pymongo import MongoClient
"""Pymongo"""


with MongoClient() as client:
    db = client.logs
    collection = db.nginx
    print("{:d} logs".format(collection.count_documents({})))
    for m in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
        print("\tmethod {:s}: {:d}"
              .format(m, collection.count_documents({"method": m})))
    print("{:d} status check"
          .format(collection
                  .count_documents({"method": "GET", "path": "/status"})))
