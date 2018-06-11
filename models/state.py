#!/usr/bin/python3
"state class module"
from .base_model import BaseModel
class State(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs) 