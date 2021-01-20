from rest_framework import serializers
from .models import *


class BoardSerializer(serializers.Serializer):
    pk = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=255)
    created_date = serializers.DateTimeField(required=False)
    modified_date = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        return Board.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.name = validate_data.get('name', instance.name)

        instance.save()
        return instance


class TaskSerializer(serializers.Serializer):
    pk = serializers.IntegerField(required=False)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=1000)
    status = serializers.BooleanField(required=False)
    created_date = serializers.DateTimeField(required=False)
    modified_date = serializers.DateTimeField(required=False)
    board_id = serializers.IntegerField()

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.title = validate_data.get('title', instance.title)
        instance.description = validate_data.get('description', instance.description)
        instance.status = validate_data.get('status', instance.status)
        instance.save()
        return instance
