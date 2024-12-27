#!/usr/bin/env python3
"""
Contains unittests for base_model module
"""
from datetime import datetime
from models.base_model import BaseModel
from unittest import TestCase


class TestBaseModel(TestCase):
    """
    Tests the BaseModel class
    """
    def setUp(self):
        """ Sets initial test conditions before each test
        """
        self.bm = BaseModel()
        return super().setUp()
    
    def tearDown(self):
        """ Resets testing conditions after each test
        """
        del self.bm
        return super().tearDown()

    def test_BaseModel(self):
        """
        Tests whether a BaseModel instance is created correctly
        """
        bm1 = BaseModel()
        self.assertIsInstance(bm1.created_at, datetime)
        self.assertEqual(bm1.updated_at, bm1.created_at)

        params = {
            'id': '1b3c52b7-1981-4e81-a75e-63af749ecb54',
            'created_at': '2024-12-18T12:41:00.241008',
            'updated_at': '2024-12-18T12:41:00.241008',
            '__class__': 'BaseModel',
            'random_attribute': 'random'
        }
        bm2 = BaseModel(**params)
        self.assertNotIn('__class__', bm2.__dict__)
        self.assertNotIn('random_attribute', bm2.__dict__)
        self.assertIsInstance(bm1.created_at, datetime)
        self.assertIsInstance(bm1.updated_at, datetime)
    
    def test_update(self):
        """
        Tests whether the instance updates correctly
        """
        self.assertEqual(self.bm.created_at, self.bm.updated_at)
        self.bm.update()
        self.assertGreater(self.bm.updated_at, self.bm.created_at)
    
    def test_to_dict(self):
        """
        Tests whether the dictionary representation of the model is returned correctly
        """
        bm_dict = self.bm.to_dict()
        self.assertIsInstance(self.bm.to_dict(), dict)
        self.assertEqual(bm_dict['__class__'], self.bm.__class__.__name__)
        self.assertIsInstance(bm_dict['created_at'], str)
        self.assertIsInstance(bm_dict['updated_at'], str)
