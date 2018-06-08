#!/usr/bin/env bash
'FileStorage module'
class FileStorage():
    'file storage class'
    __file_path = "" #path to json file
    __objects = dict()

    def all(self):
        'returns dictionary __objects'
        return self.__objects

    def new(self, obj):
        'appends an obj into the __objects dictionary'

    def save(self):
        'serializes __objects" to the JSON file (path: __file_path)'

    def reload(self):
        '''deserializes the JSON file to __objects (only if the JSON
        file exists; otherwise, do nothing'''

    
