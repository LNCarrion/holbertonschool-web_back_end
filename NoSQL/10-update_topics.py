#!/usr/bin/env python3
""" Python script to update all documents in a collection """


def update_topics(mongo_collection, name, topics):
    """ Updates all the docs in a collection based on name"""
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}

    mongo_collection.update_many(query, new_values)
