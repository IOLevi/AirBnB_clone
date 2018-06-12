#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.file_storage import FileStorage
from models.state import State
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import datetime
import pep8
import os
import json

class TestFileStorage(unittest.TestCase):
    "test class for baseModel"
    def setUp(self):
        "setup"
        pass
    
    def tearDown(self):
        "teardown"
        try:
            os.remove("files.json")
        except:
            pass
    
    def test_docstring(self):
        "tests the docstring"
        self.assertTrue(len(Basemodel.__doc__) > 1)
        self.assertTrue(len(Basemodel.__init__.__doc__) > 1)
        self.assertTrue(len(Basemodel.__str__.__doc__) > 1)
        self.assertTrue(len(Basemodel.save.__doc__) > 1)
        self.assertTrue(len(Basemodel.to_dict.__doc__) > 1)
        
    def test_pep8(self):
        "tests pep8"
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "pep8")

    def test_basic_attrs(self):
        "testing basic attributes"
        a = FileStorage()
        self.assertTrue(hasattr(a, __objects))
        b = a.all()
        self.assertEqual(type(b), dict)
        self.assertTrue(hasattr(a, __file_path))
        self.assertEqual(type(a.__dict__["_FileStorage__file_path"], str))
        self.assertTrue(len(a.__dict__["_FileStorage__file_path"] > 1))

    def test_new_method(self):
        "tests the new method"
        a = FileStorage()
        b = BaseModel()
        c = BaseModel.__class__.__name__
        d = b.id
        e = a.all()
        a.new(b)

        # check to see that it makes it c.d in the __objects dictionary
        self.assertTrue("{}.{}".format(c, d) in e)
        self.assertIs(e["{}.{}".format(c, d)], b)
    
    def test_save_method(self):
        "this is the save method"
        # opens the file (creates if doesn't exist)
        # and dumps in the __objects dictionary as a dictionary of their to_dict outputs in json format

        a = FileStorage()
        b = BaseModel()
        a.save()
        self.assertTrue(os.path.isfile("file.json"))
        with open("file.json", encoding="utf-8") as e:
            c = json.load(e)
            self.assertEqual(type(c), dict)
            for k, v in c:
                self.assertTrue("__class__" in v)
                self.assertEqual(type(v), dict)
                self.assertTrue(len(v) > 0)
                d = BaseModel(**v)
                for k, v in b.__dict__.items():
                    self.assertTrue(k in d.__dict__)
                    self.assertEqual(d.__dict__[k], b.__dict__[k])

    if __name__ == "__main__":
        unittest.main()