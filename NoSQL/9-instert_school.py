#!/usr/bin/env python3
""" Python script to insert a document into collection """


def insert_school(mongo_collection, **kwargs):
    """ Insert a doc into collection w/ kwargs 0"""
    return mongo_collection.insert_one(kwargs).inserted_id
