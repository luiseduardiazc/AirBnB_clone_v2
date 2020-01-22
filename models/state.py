#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel, Base
from models.city import City
import os
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    Class that inherits from BaseModel and Base (respect the order)
    Attributes:
        __tablename__ : represents the table name
        name: input name
    """

    __tablename__ = 'states'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", passive_deletes=True, backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """
            Return all cities in a list
            """
            list_of_cities = []
            cities = models.storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    list_of_cities.append(city)
            return list_of_cities
