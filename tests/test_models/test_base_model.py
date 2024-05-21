#!/usr/bin/python3
"""Unit tests for the BaseModel"""
###import models
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel
from time import sleep

class TestBaseModel(unittest.TestCase):
    """This class contains the Unit tests for the BaseModel class."""

    def test_initialization(self):
        """Tests whether a new BaseModel instance is properly initialized"""
        new_model = BaseModel()
        self.assertIsInstance(new_model, BaseModel)
        self.assertIsInstance(new_model.id, str)
        self.assertIsInstance(uuid.UUID(new_model.id), uuid.UUID)
        self.assertEqual(new_model.name, "")
        self.assertIsInstance(new_model.created_at, datetime)
        self.assertEqual(new_model.updated_at, new_model.created_at)


    def test_sleep_and_assert_true(self):
        """Test that sleeps for 2 seconds and always asserts True"""
        sleep(2)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
