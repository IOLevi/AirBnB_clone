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
        self.__objects.update({"{}.{}".format(obj.__class__.__name__, obj.id): obj}) 

    def save(self):
        'serializes __objects" to the JSON file (path: __file_path)'
        with open(self.__file_path, "w", encoding="utf-8") as myFile:
            dictwriter = dict()

            for k, v in self.__objects.items():
                dictwriter.update({k:v.to_dict()})
            myFile.write(json.dumps(dictwriter))

    def reload(self):
        '''deserializes the JSON file to __objects (only if the JSON
        file exists; otherwise, do nothing'''
        try:
            with open(self.__file_path, encoding="utf-8") as myFile:
                reader = json.load(myFile)
                for k, v in reader.items():
                    # m = __import__("models.base_model")
                    # TargetClass = getattr(m, v["__class__"]) #investigate reflection http://www.diveintopython.net/power_of_introspection/getattr.html
                    from ..base_model import BaseModel
                    reloadedobj = eval("{}(**v)".format(v["__class__"])) #is there a way to use the v["_class__"] to get classname dynamically
                    self.new(reloadedobj)
                
        except FileNotFoundError:
            pass #do nothing when there is no file

    
