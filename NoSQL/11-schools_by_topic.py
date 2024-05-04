#!/usr/bin/env python3
""" Python script that returns the list of school having a specific topic """


def schools_by_topic(mongo_collection, topic):
    """ Specific topic goes here """
    documents = mongo_collection.find({"topics": topic})
    list_docs = [d for d in documents]
    return list_docs