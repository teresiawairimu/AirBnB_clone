#!/usr/bin/python3
"""Unit tests for the BaseModel"""
import unittest
import models
from models.base_model import BaseModel
from datetime import datetime
import uuid


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


if __name__ == '__main__':
    unittest.main()
