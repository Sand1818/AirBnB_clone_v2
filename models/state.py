#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all,delete", backref="state")

    @property
    def cities(self):
        """Gets attribute for cities"""
        dolophu = models.storage.all(City)
        list = []
        for key, value in dolophu.items():
            if value.state_id == self.id:
                list.append(value)
        return list
