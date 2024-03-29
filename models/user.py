#!/usr/bin/python3
"""This module defines
    a class User
    to manipulate instances
    and create and destroy
    """
from models.base_model import BaseModel


class User(BaseModel):
    """
    This class defines a user
        by various attributes
        """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
