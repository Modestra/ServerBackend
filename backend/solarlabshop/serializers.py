from rest_framework import serializers
from solarlabshop.models import *

class CategoryChildSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categories
        fields = ("name", "parentid")
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'
        read_only_fields = ["category_id"]

class AdvertSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advert
        fields = '__all__'
        read_only_fields = ['advert_id']
class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = '__all__'
        read_only_fields = ["image_id"]
    
class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comments
        fields = '__all__'

