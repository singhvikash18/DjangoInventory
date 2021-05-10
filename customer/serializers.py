from rest_framework import serializers
from .models import Emplyoee,ItemGroup

class EmplyoeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Emplyoee
        fields = '__all__'

class ItemGroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = ItemGroup
        fields = '__all__'