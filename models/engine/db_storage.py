#!/usr/bin/python3
"""This is the db storage class for AirBnB"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __engine = None
    __session = None

    def __init__(self):
        """ Init method """

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                      getenv("HBNB_MYSQL_USER"),
                                      getenv("HBNB_MYSQL_PWD"),
                                      getenv("HBNB_MYSQL_HOST"),
                                      getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query a clase type """

        ans = {}
        if cls is None:
            for i in self.__session.query(User,
                                          State, City, Place,
                                          Amenity, Review).all():
                print("object:   {}".format(i))
                ans["{}.{}".format(type(i).__name__, i.id)] = i
        else:
            for i in self.__session.query(cls).all():
                ans["{}.{}".format(type(i).__name__, i.id)] = i
        return ans

    def new(self, obj):
        """add the object to the current database session """

        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session """

        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None """

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
