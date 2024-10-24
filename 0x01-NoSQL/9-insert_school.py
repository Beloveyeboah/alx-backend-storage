#!/usr/bin/env python3

"""
Python function that inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into a MongoDB collection.
    :param mongo_collection: The pymongo collection object
    :param kwargs: Keyword arguments representing
    the document fields and values
    :return:The _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
