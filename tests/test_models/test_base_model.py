#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
import datetime
import pep8
import os

class TestBaseModel(unittest.TestCase):
    "test class for baseMoldel"
    def setUp(self):
        "setup"
        pass
    
    def tearDown(self):
        "teardown"
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

    def test_init_args_not_used(self):
        "make sure args are not used"
        a = BaseModel(12)
        self.assertEqual(type(a).__name__, "BaseModel")
        self.assertFalse(hasattr(a, 12))
    
    def test_init_kwargs_correct(self):
        "make sure kwargs are used correctly"
        v = {"b": 123}
        a = BaseModel(**v)
        self.assertFalse(hasattr(a, "id"))
        self.assertFalse(hasattr(a, "updated_at"))
        self.assertFalse(hasattr(a, "created_at"))
        self.assertTrue(hasattr(a, "b"))

    def test_NumberThree(self):
        "testing items from problem 3"
        a = BaseModel()
        b = BaseModel()
        self.assertEqual(type(a.id), str)
        self.assertNotEqual(a.id, b.id)
        self.assertEqual(type(a.created_at), datetime.datetime)
        self.assertEqual(type(a.updated_at), datetime.datetime)
        
    if __name__ == "__main__":
        unittest.main()

    