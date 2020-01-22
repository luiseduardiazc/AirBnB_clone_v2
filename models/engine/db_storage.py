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

all_classes = {"User": User, "State": State, "City": City,
               "Amenity": Amenity, "Place": Place, "Review": Review}


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
        """ Init method
    Attributes:
        __engine: engine for SQLAlchemy
        __session: session to work"""

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                      getenv("HBNB_MYSQL_USER"),
                                      getenv("HBNB_MYSQL_PWD"),
                                      getenv("HBNB_MYSQL_HOST"),
                                      getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of objects
        """

        ans = {}
        if cls is None:
            for _class in all_classes.values():
                query = self.__session.query(_class).all()
                for item in query:
                    ans["{}.{}".format(_class.__name__, item.id)] = item
        else:
            for i in self.__session.query(cls).all():
                ans["{}.{}".format(type(i).__name__, i.id)] = i
        return ans

    def new(self, obj):
        """add the object to the current database session
        Args:
            obj: given object
        """
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

    def close(self):
        '''
        close session
        '''
        self.__session.close()
