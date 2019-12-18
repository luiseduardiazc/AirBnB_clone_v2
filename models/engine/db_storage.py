#!/usr/bin/python3
"""This is the db storage class for AirBnB"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models
from models.base_model import BaseModel, Base

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
                                      getenv(HBNB_MYSQL_USER),
                                      getenv(HBNB_MYSQL_PWD),
                                      getenv(HBNB_MYSQL_HOST),
                                      getenv(HBNB_MYSQL_DB)),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)
        

    def all(self, cls=None):
        """Query a clase type """

        Session = sessionmaker(bind=engine)
        self.__session = Session()
        ans = {}
        if cls is not None:
            for i in self.__session.query(cls).all():
                ans["{}.{}".format(type(i).__name__, i.id)] = i
        else:
            for i in self.__session.all():
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
        Base.metadata.create_all(engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()