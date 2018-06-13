#!/usr/bin/python3
"state class module"
from .base_model import BaseModel
class State(BaseModel):
    "state class"
    name = ""

    def __init__(self, *args, **kwargs):
        "state init"
        super().__init__(**kwargs) 