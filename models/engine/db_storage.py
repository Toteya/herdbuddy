#!/usr/bin/env python3
"""
db_storage module: contains the MongoDB storage engine implementation
"""
from pymongo import MongoClient
from os import environ


class DBStorage:
    """
    A storage engine that interacts interacts with the MongoDB database
    containing all the application data
    """
    __client = None
    def __init__(self):
        database = environ.get('HERDBUDDY_DB')
        host = environ.get('HERDBUDDY_HOST', 'localhost')
        port = environ.get('HERDBUDDY_PORT', 12017)
        self.__client = MongoClient(f'mongodb://{host}:{port}')
    
    def all(self, clss=None):
        """
        Returns a dictionary containing all objects of the given. If no class
        specified, it returns all objects from all classes
        """
        # obj_list = []
        # if clss is not None:
        #     obj_list = self.__client
    
    def get(self, clss=None, id=None):
        """
        Returns an object based on the given id
        """
        if not all([clss, id]):
            return None
        # obj =