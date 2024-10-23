#!/usr/bin/env python3

"""
Python function that returns
the list of school having a specific topic
"""

import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Return a list of schools having a specific topic.

    :param mongo_collection: The pymongo collection object
    :param topic: The topic searched
    :return: A list of schools with the specific topic
    """
    return list(mongo_collection.find({"topics": topic}))
