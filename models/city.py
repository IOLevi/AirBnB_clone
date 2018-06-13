#!/usr/bin/python3
"city class module"
from .base_model import BaseModel

class City(BaseModel):
    "city class"
    state_id=""
    name=""
    def __init__(self, *args, **kwargs):
        "init method"
        super().__init__(**kwargs)