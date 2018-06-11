#!/usr/bin/python3
"amenity class module"
from .base_model import BaseModel
class Amenity(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs) 
