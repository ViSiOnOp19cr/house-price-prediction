import sys

from house.exception import exception
from house.logger import logging

import os
from house.constants import DATABASE_NAME,MONGODB_URL_KEY
import pymongo
import certifi

ca = certifi.where()

class MongoDBClinet:
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClinet.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise exception(f"environment key: {MONGODB_URL_KEY} is not set.")
                MongoDBClinet.client = pymongo.MongoClient(mongo_db_url,tlsCAFile=ca)
            self.client = MongoDBClinet.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("mongodb connection successfull")
        except exception as e:
            raise exception(e,sys)