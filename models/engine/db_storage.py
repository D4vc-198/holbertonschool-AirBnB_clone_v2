#!/usr/bin/python3
"""Module for DBstorage class"""
from os import getenv
from sqlalchemy import create_engine, MetaData


class DBStorage():
    """Class for database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes storage"""
        from models.base_model import Base
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(getenv("HBNB_MYSQL_USER"),
                    getenv("HBNB_MYSQL_PWD"),
                    getenv("HBNB_MYSQL_HOST"),
                    getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)
