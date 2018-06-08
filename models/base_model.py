#!/usr/bin/env bash

'BaseModel module'
import uuid
import datetime

class BaseModel():
    'BaseModel class'
    def __init__(self):
        'initialization'
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        'to string magic method'
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        'updates the public instance attributed updated_at w/ current time'
        self.updated_at = datetime.datetime.now()


    def to_dict(self):
        'returns a dictionary containing all key/values of __dict__'
        a = self.__dict__.copy()
        a["__class__"] = self.__class__.__name__
        a["created_at"] = a["created_at"].isoformat()
        a["updated_at"] = a["updated_at"].isoformat()
        return a




