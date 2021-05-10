from rest_framework import viewsets
from . import models
from . import serializers

class EmplyoeeViewset(viewsets.ModelViewSet):
    queryset = models.Emplyoee.objects.all()
    serializer_class = serializers.EmplyoeeSerializers
    
class ItemGroupViewset(viewsets.ModelViewSet):
    queryset = models.ItemGroup.objects.all()
    serializer_class = serializers.ItemGroupSerializers    