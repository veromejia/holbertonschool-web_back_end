#!/usr/bin/env python3
"""inserts a new document in a collection based on kwargs"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """mongo_collection will be the pymongo
    returns a new id"""
    new_doc = mongo_collection.insert(kwargs)
    return new_doc
