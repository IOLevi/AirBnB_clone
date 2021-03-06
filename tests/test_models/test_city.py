#!/usr/bin/python3
"City test module"
import unittest
from models.base_model import BaseModel
from models.city import City
import datetime
import pep8
import os


class TestCity(unittest.TestCase):
    "test class for City"

    def setUp(self):
        "setup"
        pass

    def tearDown(self):
        "teardown"
        pass

    def test_docstring(self):
        "tests the docstring"
        self.assertTrue(len(BaseModel.__doc__) > 1)
        self.assertTrue(len(BaseModel.__init__.__doc__) > 1)
        self.assertTrue(len(BaseModel.__str__.__doc__) > 1)
        self.assertTrue(len(BaseModel.save.__doc__) > 1)
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 1)

    def test_has_class_attrs(self):
        a = City()
        self.assertTrue("name" in dir(a)) # looking for the class variables it said to make
        #dir(a)
    def test_pep8(self):
        "tests pep8"
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "pep8")

if __name__ == "__main__":
    unittest.main()
