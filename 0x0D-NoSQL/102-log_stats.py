#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    with MongoClient() as client:
        """Mongodb Client"""
        db = client.logs
        collection = db.nginx
        print("{:d} logs".format(collection.count_documents({})))
        print("Methods:")
        for m in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
            print("\tmethod {:s}: {:d}"
                  .format(m, collection.count_documents({"method": m})))
        print("{:d} status check"
              .format(collection
                      .count_documents({"method": "GET", "path": "/status"})))
        ips = collection.aggregate([{
            '$group': {
                '_id': '$ip',
                'count': {
                    '$sum': 1
                }
            }
        }, {
            '$sort': {
                'count': -1
            }
        }, {
            '$limit': 10
        }])

    print("IPs:")
    for ip in ips:
        print("\t{:s}: {:d}".format(ip.get("_id"), ip.get("count")))
