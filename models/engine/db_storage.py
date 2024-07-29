#!/usr/bin/python3
"""Defines a DBStorage engine"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import os


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        USER = os.getenv('HBNB_MYSQL_USER')
        PWD = os.getenv('HBNB_MYSQL_PWD')
        HOST = os.getenv('HBNB_MYSQL_HOST')
        DB = os.getenv('HBNB_MYSQL_DB')
        conn_uri = f'mysql+mysqldb://{USER}:{PWD}@{HOST}/{DB}'
        self.__engine = create_engine(conn_uri, pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        obj_dict = {}
        classes = [User, Place, Review, Amenity, State, City]
        if cls is not None:
            query_obj = self.__session.query(cls)
            for obj in query_obj.all():
                obj_dict[f"{obj.__class__.__name__}.{obj.id}"] = obj
            return obj_dict
        else:
            for clss in classes:
                query_obj = self.__session.query(clss).all()
                for obj in query_obj:
                    obj_dict[f"{obj.__class__.__name__}.{obj.id}"] = obj
            return obj_dict

    def new(self, obj):
        """add the object to the current database session"""
        if obj is not None:
            self.__session.add(obj)
            self.__session.flush()
            self.__session.refresh(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj):
        """delete from the current database session"""
        if obj:
            self.__session.query(type(obj)
                                 .filter(type(obj) == obj.id)
                                 .delete(obj))

    def reload(self):
        """creates all tables from database"""
        Base.metadata.create_all(self.__engine)
        sessionfactory = sessionmaker(
                            bind=self.__engine,
                            expire_on_commit=False)
        Session = scoped_session(sessionfactory)
        self.__session = Session()

    def close(self):
        """closes session"""
        self.__session.close()
