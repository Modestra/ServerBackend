from Vasiliq.models import *
from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ["client_id"]

class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdminModel
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model =Order
        fields = '__all__'
        read_only_fields = ["order_id"]

class MedicamentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medicament
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'