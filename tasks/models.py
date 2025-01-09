from bson import ObjectId
from datetime import datetime
from .db import get_mongo_client

class Task:
    def __init__(self, description, status, user, _id=None):
        # Usamos ObjectId() solo si no se pasa uno
        self._id = _id if _id else ObjectId()
        self.description = description
        self.status = status
        self.user = user
        self.created_at = datetime.now()
    
    def save(self):
        db = get_mongo_client()
        collection = db.tasks

        if self._id:
            collection.update_one(
                {"_id": self._id},
                {"$set": self.__dict__}
            )
            print(f"Task with ID {self._id} updated.")
        else:
            result = collection.insert_one(self.__dict__)
            self._id = result.inserted_id
            print(f"Task with ID {self._id} inserted.")
    
    @staticmethod
    def get_all_tasks():
        db = get_mongo_client()
        collection = db.tasks
        tasks = collection.find()
        return [{**task, "_id": str(task["_id"])} for task in tasks]
    
    @staticmethod
    def get_task_by_id(task_id):
        db = get_mongo_client()
        collection = db.tasks
        task = collection.find_one({"_id": ObjectId(task_id)})
        if task:
            task["_id"] = str(task["_id"])
        return task

    @staticmethod
    def update_task(task_id, update_data):
        db = get_mongo_client()
        collection = db.tasks
        collection.update_one(
            {"_id": ObjectId(task_id)}, 
            {"$set": update_data}
        )
    
    @staticmethod
    def delete_task(task_id):
        db = get_mongo_client()
        collection = db.tasks
        collection.delete_one({"_id": ObjectId(book_id)})
        print(f"Task with ID {task_id} marked as deleted.")
