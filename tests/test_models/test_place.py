#!/usr/bin/python3
"Place test module"
import unittest
from models.base_model import BaseModel
from models.place import Place
import datetime
import pep8
import os


class TestPlace(unittest.TestCase):
    "test class for Place"

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
        a = Place()
        self.assertTrue("city_id" in dir(a)) # looking for the class variables it said to make
        self.assertTrue("user_id" in dir(a))
        self.assertTrue("name" in dir(a))
        self.assertTrue("description" in dir(a))
        self.assertTrue("number_rooms" in dir(a))
        self.assertTrue("number_bathrooms" in dir(a))
        self.assertTrue("max_guest" in dir(a))
        self.assertTrue("price_by_night" in dir(a))
        self.assertTrue("latitude" in dir(a))
        self.assertTrue("longitude" in dir(a))
        self.assertTrue("amenity_ids" in dir(a))

    def test_pep8(self):
        "tests pep8"
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "pep8")

if __name__ == "__main__":
    unittest.main()
