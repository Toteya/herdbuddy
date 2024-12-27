#!/usr/bin/env python3
"""
user module: User account model implements
"""
from base_model import BaseModel


class User(BaseModel):
    """
    A user account
    Inherits BaseModel
    """
    emai = ''
    password = ''
