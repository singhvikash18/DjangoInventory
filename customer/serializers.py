from rest_framework import serializers
from .models import Emplyoee,ItemGroup,Invoice

class EmplyoeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Emplyoee
        fields = '__all__'

class ItemGroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = ItemGroup
        fields = '__all__'

class InvoiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'        