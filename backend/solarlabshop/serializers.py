from rest_framework import serializers
from solarlabshop.models import *

class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'

class AdvertSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advert
        flelds = '__all__'