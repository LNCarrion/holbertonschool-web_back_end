#!/usr/bin/env python3
""" Python script to list all docs in MongoDB """


def list_all(mongo_collection):
    """ List all docs in collection """
    return [doc for doc in mongo_collection.find()]