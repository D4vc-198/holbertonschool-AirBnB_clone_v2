#!/usr/bin/python3
"""test for database storage"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from os import getenv


class TestDBStorage(unittest.TestCase):
    """ Test DBStorage """

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Diego"
        cls.user.last_name = "Valdez"
        cls.user.email = "diego1234@gmail.com"
        cls.storage = DBStorage()

    @classmethod
    def teardown(cls):
        del cls.user

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                        "Not using db")
    
        @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "Not using db")
    def test_pep8_DBStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "Not using db")

    def test_all(self):
        """tests if all works in File Storage"""
        storage = DBStorage()
        storage.reload()
        dict_len = len(storage.all())
        s = State(name="test_all_state")
        s.save()
        storage.save()
        self.assertIs(len(storage.all()), dict_len + 1)