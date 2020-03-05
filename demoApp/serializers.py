from rest_framework import serializers

from demoApp.models import Owner, Cat, Dog


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'
