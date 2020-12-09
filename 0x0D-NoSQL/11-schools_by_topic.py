#!/usr/bin/env python3
"""11-schools_by_topic"""


def schools_by_topic(mongo_collection, topic):
    """ Return lists of schools that have a specific topic """
    return mongo_collection.find({"topics": topic})
