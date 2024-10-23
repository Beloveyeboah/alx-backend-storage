#!/usr/bin/env python3

"""
a Python function that returns all students sorted by average score
"""


import pymongo


from pymongo import MongoClient


def top_students(mongo_collection):
    """
    Return all students sorted by average score.

    :param mongo_collection: The pymongo collection object
    :return: A list of students sorted by average score
    """
    pipeline = [
        {
            "$project": {
                "name": 1,
                "averageScore": {"$avg": "$scores"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ]

    return list(mongo_collection.aggregate(pipeline))


if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")
    db = client.my_db
    students_collection = db.students

    top_students_list = top_students(students_collection)
    for student in top_students_list:
        print(student)
