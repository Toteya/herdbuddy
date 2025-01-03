#!/usr/bin/env python3
"""
module cow: Implementation of livestock cow
"""
from base_model import BaseModel


class Cow(Animal):
    """
    A livestock type: cow
    """
    mother_id = None
    dehorned = False
    weaned = False
    month_of_birth = None
    medical_history = {'vaccinations': [], 'treatments': []}
