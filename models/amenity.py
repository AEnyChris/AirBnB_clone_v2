#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import os

class Amenity(BaseModel, Base):
    """Creates an amenity object"""
    __tablename__ = 'amenities'

    name = Column(
            String(128), nullable=False
            ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ""
