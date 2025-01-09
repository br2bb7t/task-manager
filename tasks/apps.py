from django.apps import AppConfig
from .insert_tasks import insert_initial_tasks


class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'
    
    def ready(self):
        insert_initial_tasks()

