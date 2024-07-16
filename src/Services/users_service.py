# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/15
🚀 Welcome to the Awesome Python Script 🚀

User: mesabo
Email: mesabo18@gmail.com / messouaboya17@gmail.com
Github: https://github.com/mesabo
Univ: Hosei University
Dept: Science and Engineering
Lab: Prof YU Keping's Lab
"""

from datetime import datetime
from typing import List
from bson import ObjectId
from ..Database.db_config import Database
from ..Models.users_model import UsersModel

class UsersService:
    def __init__(self):
        db_manager = Database()
        self.db = db_manager.get_db()

    def insertOne(self, element: UsersModel, collection_name: str) -> str:
        element.created_at = datetime.now()
        element.updated_at = datetime.now()
        inserted = self.db[collection_name].insert_one(element.to_mongo())
        return str(inserted.inserted_id)

    def insertMany(self, elements: List[UsersModel], collection_name: str) -> list[str]:
        for element in elements:
            element.created_at = datetime.now()
            element.updated_at = datetime.now()
        mongo_data = [element.to_mongo() for element in elements]
        inserted = self.db[collection_name].insert_many(mongo_data)
        return [str(id) for id in inserted.inserted_ids]

    def find(self, criteria, collection_name, projection=None, sort=None, limit=0, cursor=False):
        if "id" in criteria:
            criteria["_id"] = ObjectId(criteria.pop("id"))
        found = self.db[collection_name].find(filter=criteria, projection=projection, sort=sort, limit=limit)
        if cursor:
            return found
        found = list(found)
        for i in range(len(found)):
            if "_id" in found[i]:
                found[i]["id"] = str(found[i].pop("_id"))
        return found

    def findById(self, id, collection_name):
        found = self.db[collection_name].find_one({"_id": ObjectId(id)})
        if found is None:
            return None
        if "_id" in found:
            found["id"] = str(found.pop("_id"))
        return found

    def update(self, id, element: UsersModel, collection_name: str) -> str:
        criteria = {"_id": ObjectId(id)}
        element.updated_at = datetime.now()
        if "id" in element:
            del element["id"]
        set_obj = {"$set": element.to_mongo()}
        updated = self.db[collection_name].update_one(criteria, set_obj)
        if updated.matched_count == 1:
            return f"Record updated successfully: {updated.upserted_id}"
        else:
            return f"Unable to update the record: {id}"

    def deleteOne(self, id, collection_name: str) -> str:
        criteria = {"_id": ObjectId(id)}
        deleted = self.db[collection_name].delete_one(criteria)
        if deleted.deleted_count == 1:
            return f"Record deleted successfully: {id}"
        else:
            return f"Unable to delete the record: {id}"

    def deleteMany(self, ids: List[str], collection_name: str) -> List[str]:
        results = []
        for id in ids:
            criteria = {"_id": ObjectId(id)}
            deleted = self.db[collection_name].delete_one(criteria)
            if deleted.deleted_count == 1:
                results.append(f"Record deleted successfully: {id}")
            else:
                results.append(f"Unable to delete the record: {id}")
        return results