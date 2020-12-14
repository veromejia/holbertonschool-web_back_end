#!/usr/bin/env python3
"""function that return all students sorted by average score"""
import pymongo


def top_students(mongo_collection):
    """find and sort by average"""
    return mongo_collection.aggregate([
        {"$project": {"name": "$name", "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}}
    ])
