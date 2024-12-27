#!/usr/bin/env python3
"""
animal module: Animal model implementation
"""
from base_model import BaseModel


class Animal(BaseModel):
    """
    An animal / livestock
    """
    type = ''
    tag_id = ''
    owner_id = ''
    age = 0
