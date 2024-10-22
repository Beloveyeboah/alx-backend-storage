#!/usr/bin/env python3

"""
function that lists all documents in a collection
"""

import pymongo


def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection.

    :param mongo_collection: The pymongo collection object
    :return: A list of all documents in the collection
    """
    documents = list(mongo_collection.find())
    if not documents:
        return []
    return documents
