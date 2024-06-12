from house.configuration.mongo_db_connection import MongoDBClient

from house.constants import DATABASE_NAME
from house.exception import exception
import pandas as pd
import sys
from typing import Optional
import numpy as np

class house:
    def __init__(self):
        try:
            self.mongo_client = MongoDBClient(Database_name = DATABASE_NAME)
        except exception as e:
            raise exception(e,sys)
    def export_collection_as_dataframe(self,collection_name:str, database_name:Optional[str]=None)->pd.DataFrame:
        try:
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)
            df.replace({"na":np.nan},inplace=True)
            return df
        except exception as e:
            raise exception(e,sys)