#!/usr/bin/python3
"User class module"

from .base_model import BaseModel

class User(BaseModel):
    "User class"
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        "User init"
        super().__init__(**kwargs) #should i pass through kwargs here
        