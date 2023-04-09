#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database


if __name__ == "__main__":
    with MongoClient() as client:
        """Mongodb Client"""
        db = client.logs
        collection: Collection = db.nginx
        print("{:d} logs".format(collection.count_documents({})))
        print("Methods:")
        for m in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
            print("\tmethod {:s}: {:d}"
                  .format(m, collection.count_documents({"method": m})))
        print("{:d} status check"
              .format(collection
                      .count_documents({"method": "GET", "path": "/status"})))
