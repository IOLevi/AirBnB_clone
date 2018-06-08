#!/usr/bin/env bash

'BaseModel module'
import uuid
import datetime
from engine import storage

class BaseModel():
    'BaseModel class'

    def __init__(self, *args, **kwargs):
        'initialization'
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)

    def __str__(self):
        'to string magic method'
        return "[{}] ({}) {}".format(
    self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        'updates the public instance attributed updated_at w/ current time'
        self.updated_at=datetime.datetime.now()
        storage.save(self) #whats the right order of these two lines


    def to_dict(self):
        'returns a dictionary containing all key/values of __dict__'
        a=self.__dict__.copy()
        a["__class__"]=self.__class__.__name__
        a["created_at"]=a["created_at"].isoformat()
        a["updated_at"]=a["updated_at"].isoformat()
        return a
