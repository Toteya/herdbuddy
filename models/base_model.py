#!/usr/bin/env python3
"""
base_model module: Base model implemeentation
"""
from datetime import datetime
# import hashlib
import uuid


class BaseModel():
    """
    The base class (parent class) for all models
    """

    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at':
                    self.created_at = datetime.strptime(value, time_format)
                if key == 'updated_at':
                    self.updated_at = datetime.strptime(value, time_format)
                    continue
                if hasattr(self, key):
                    setattr(self, key, value)
            # Implement password storage e.g. SHA1
            # if kwargs.get('password') and isinstance(self.password, str):
            #     try:
            #         hash_object = hashlib.md5(bytes.fromhex(self.password))
    
    def update(self):
        """ Updates the attributes
        """
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """
        Return a dictionary representation of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = datetime.isoformat(self.created_at)
        obj_dict['updated_at'] = datetime.isoformat(self.updated_at)
        obj_dict['__class__'] = self.__class__.__name__
        if obj_dict.get('_sa_instance_state'):
            del obj_dict['_sa_instance_state']
        return obj_dict
