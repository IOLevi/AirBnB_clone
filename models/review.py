#!/usr/bin/python3
"review class module"
from .base_model import BaseModel
class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs) 
