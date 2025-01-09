from rest_framework import serializers

class TaskSerializer(serializers.Serializer):
    _id = serializers.CharField()
    description = serializers.CharField(max_length=255)
    status = serializers.CharField(max_length=50)
    user = serializers.CharField(max_length=100)
    created_at = serializers.DateTimeField(read_only=True)
