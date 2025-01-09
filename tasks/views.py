from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from bson import ObjectId  # To work with ObjectId in MongoDB

class TaskListCreate(APIView):
    def get(self, request):
        tasks = Task.get_all_tasks()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task_data = serializer.validated_data
            task = Task(**task_data)
            task.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):
    def get(self, request, pk):
        task = Task.get_task_by_id(pk)
        if task:
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        update_data = request.data
        Task.update_task(pk, update_data)
        return Response(update_data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        Task.delete_task(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
