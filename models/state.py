#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    id =  Column(Integer, primary_key=True, autoincrement=True,
                 nullable=False)
    name = Column(String(128), nullable=False)
    #cities = relationship("City", cascade="all,delete", backref="state")
