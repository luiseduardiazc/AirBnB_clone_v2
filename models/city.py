#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.state import State

class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    id =  Column(Integer, primary_key=True, autoincrement=True,
                 nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
    name = Column(String(128), nullable=False)
    #places = relationship("Place", cascade="all,delete", backref="cities")
