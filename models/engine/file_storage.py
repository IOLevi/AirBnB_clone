#!/usr/bin/env bash
'FileStorage module'

import json

class FileStorage():
    'file storage class'
    __file_path = "file.json" #path to json file
    __objects = dict() #stores objects by <classname>.id:obj

    def all(self):
        'returns dictionary __objects'
        return self.__objects

    def new(self, obj):
        'adds an obj into the __objects dictionary'
        self.__objects.update("{}.{}".format(obj.__class__.__name__, obj.id), obj) 

    def save(self):
        'serializes __objects" to the JSON file (path: __file_path)'
        with open(self.__file_path, "w", encoding="utf-8") as myFile:
            myFile.write(json.dumps(self.__objects))

    def reload(self):
        '''deserializes the JSON file to __objects (only if the JSON
        file exists; otherwise, do nothing'''
        try:
            with open(self.__file_path, encoding="utf-8") as myFile:
                self.__objects = json.load(myFile)
        except FileNotFoundError:
            pass #do nothing when there is no file

    
