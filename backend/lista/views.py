from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from lista.models import Item
from lista.serializers import ItemSerializer

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer