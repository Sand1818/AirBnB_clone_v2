#!/usr/bin/python3
"""DB Storage"""
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """DB Storage class"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialise new db instance."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on bd"""
        if cls is None:
            query = self.__session.query(State).all()
            query.extend(self.__session.query(City).all())
            query.extend(self.__session.query(User).all())
            query.extend(self.__session.query(Place).all())
            query.extend(self.__session.query(Review).all())
            query.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            query = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in query}

    def new(self, obj):
        """adds obj to db"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to db"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes obj from db"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """crete table in db"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """closes SQLAlchemy session."""
        self.__session.close()