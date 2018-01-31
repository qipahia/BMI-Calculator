__author__='akishan'

import uuid
import datetime
from common.database import Database

class User(object):
    def __init__(self,user_name,height,weight,_id=None):
        self.user_name=user_name
        self.height=height
        self.weight=weight
        self._id= uuid.uuid4().hex if _id is None else _id

    def json(self):
        return{'user_name':self.user_name,
		'height':self.height,
		'weight':self.weight,
		'_id':self._id}

    def save_to_mongo(self):
        Database.insert(collection='user_data',data=self.json())

    @classmethod
    def find_by_id(cls,_id):
        data=Database.find_one(collection='user_data', query={'_id':_id})
      
        return cls(**data)
	

