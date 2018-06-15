#!/usr/bin/python3
"City test module"
import unittest
from models.base_model import BaseModel
from models.user import User
import datetime
import pep8
import os


class TestUser(unittest.TestCase):
    "test class for User"

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
        a = User()
        self.assertTrue("email" in dir(a))
        self.assertTrue("password" in dir(a))
        self.assertTrue("first_name" in dir(a))
        self.assertTrue("last_name" in dir(a))


    def test_pep8(self):
        "tests pep8"
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "pep8")

if __name__ == "__main__":
    unittest.main()
