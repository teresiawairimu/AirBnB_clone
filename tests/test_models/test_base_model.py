#!/usr/bin/python3
"""Unit tests for the BaseModel"""
# import models
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

    def test_save(self):
        """Tests the save method's functionality"""
        new_model = BaseModel()
        initial_updated_time = new_model.updated_at
        new_model.save()
        self.assertNotEqual(new_model.updated_at, initial_updated_time)
        self.assertIsInstance(new_model.updated_at, datetime)

    def test_to_dict(self):
        """Tests the to_dict method's functionality"""
        new_model = BaseModel()
        data = new_model.to_dict()
        self.assertIsInstance(data, dict)
        self.assertIn('__class__', data)
        self.assertEqual(data['__class__'], 'BaseModel')
        self.assertIn('id', data)
        self.assertEqual(data['id'], new_model.id)
        self.assertIn('name', data)
        self.assertEqual(data['name'], new_model.name)
        self.assertIn('created_at', data)
        self.assertEqual(data['created_at'], new_model.created_at.isoformat())
        self.assertIn('updated_at', data)
        self.assertEqual(data['updated_at'], new_model.updated_at.isoformat())

    def test_sleep_and_assert_true(self):
        """Test that sleeps for 2 seconds and always asserts True"""
        sleep(2)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
