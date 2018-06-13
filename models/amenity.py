#!/usr/bin/python3
"amenity class module"
from .base_model import BaseModel
class Amenity(BaseModel):
    "amenity class"
    name = ""

    def __init__(self, *args, **kwargs):
        "amenity init"
        super().__init__(**kwargs) 
