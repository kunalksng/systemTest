from rest_framework import serializers


class CreateNameSerializer(serializers.Serializer):
    name = serializers.JSONField()
    address=serializers.JSONField()
    phone = serializers.JSONField()
    email = serializers.CharField(max_length=100)


class UpdateContactSerializer(serializers.Serializer):
    name = serializers.JSONField(required=False)
    address=serializers.JSONField(required=False)
    phone = serializers.JSONField(required=False)
    email = serializers.CharField(max_length=100,required=False)
