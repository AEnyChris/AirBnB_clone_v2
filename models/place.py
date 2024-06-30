#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy import Float
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models.review import Review
import os


place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column(
            'place_id',
            String(60),
            ForeignKey('places.id'),
            primary_key=True,
            nullable=True),
        Column(
            'amenity_id',
            String(60),
            ForeignKey('amenities.id'),
            primary_key=True,
            nullable=True)
        )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(
                String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(
                String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship(
                'Review',
                backref='place',
                cascade='all, delete-orphan')
        amenities = relationship(
                'Amenity',
                secondary=place_amenity,
                backref='place',
                viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """returns a list of reviews for a given place"""
            from models import storage
            review_list = []
            review_objects = storage.all(Review)
            for obj in review_obj.values():
                if obj.place_id == self.id:
                    review_list.append(obj)
            return review_list

        @property
        def amenities(self):
            """returns a list of amenities associated with place"""
            from models import storage
            place_amenity_list = []
            for obj in storage.all(Amenity).values():
                if obj.id in self.amenity_ids:
                    place_amenity_list.append(obj.id)
            return place_amenity_list

        @amenities.setter
        def amenitiies(self, obj):
            """adding amentiy to a place"""
            if type(obj) == Amenity:
                if obj.id not in self.amenity_ids:
                    self.amenity_ids.append(obj.id)
