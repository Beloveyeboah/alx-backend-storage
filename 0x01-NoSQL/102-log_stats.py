#!/usr/bin/env python3

""" improved"""

import pymongo
from pymongo import MongoClient


def log_stats():
    """
    Provide stats about Nginx logs stored in MongoDB and
    list the top 10 most present IPs.
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
    method_counts = {method: collection.count_documents({"method": method})
                     for method in methods}

    # Print method counts
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")

    # Count documents with method=GET and path=/status
    get_status_count = collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{get_status_count} status check")

    # Get the top 10 most present IPs
    top_ips_pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = list(collection.aggregate(top_ips_pipeline))

    # Print top 10 IPs
    print("IPs:")
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    log_stats()
