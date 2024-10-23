#!/usr/bin/env python3

"""
Python function that changes all topics of a school
document based on the name
"""

import pymongo


def update_topics(mongo_collection, name, topics):
    """
    Update the topics of a school
    document based on the school name.

    :param mongo_collection: The pymongo collection object
    :param name: The school name to update
    :param topics: List of topics to set in the document
    """
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
