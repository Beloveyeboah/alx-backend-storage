#!/usr/bin/env python3

"""
Python script that provides some stats about
Nginx logs stored in MongoDB
"""

import pymongo
from pymongo import MongoClient


def print_nginx_stats():
    """  return: 
    """

    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client.logs
    collection = db.nginx

    # Get the total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Initialize a dictionary to count methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method}) for method in methods}

    # Print method counts
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")

    # Count documents with method=GET and path=/status
    get_status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{get_status_count} status check")

if __name__ == "__main__":
    print_nginx_stats()
