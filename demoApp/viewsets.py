from rest_framework.viewsets import ModelViewSet

from demoApp.models import Owner, Cat, Dog
from demoApp.serializers import OwnerSerializer, DogSerializer, CatSerializer


class OwnerViewSet(ModelViewSet):
    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()


class DogViewSet(ModelViewSet):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()


class CatViewSet(ModelViewSet):
    serializer_class = CatSerializer
    queryset = Cat.objects.all()