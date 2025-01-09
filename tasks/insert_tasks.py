from .models import Task
from .db import get_mongo_client
from datetime import datetime

def insert_initial_tasks():
    tasks_data = [
        {"description": "Task 1", "status": "Pending", "user": "User 1", "created_at": datetime.now()},
        {"description": "Task 2", "status": "In Progress", "user": "User 2", "created_at": datetime.now()},
        {"description": "Task 3", "status": "Completed", "user": "User 3", "created_at": datetime.now()},
        {"description": "Task 4", "status": "Pending", "user": "User 4", "created_at": datetime.now()},
        {"description": "Task 5", "status": "In Progress", "user": "User 5", "created_at": datetime.now()}
    ]

    # Connect to MongoDB and select the tasks collection
    db = get_mongo_client()
    collection = db.tasks

    # Check if there are any tasks already, to prevent duplication
    if collection.count_documents({}) == 0:
        # Insert tasks into the collection
        collection.insert_many(tasks_data)
        print("Initial tasks data inserted.")
    else:
        print("Tasks data already exists.")

# Run the migration script (this can be called manually, or as part of the app setup)
if __name__ == "__main__":
    insert_initial_tasks()
