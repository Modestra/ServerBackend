from rest_framework import serializers
from solarlabshop.models import *

class CategoryChildSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categories
        fields = ("name", "parentid")
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = ("name", "parentid")

class CategoryAllSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'

class AvitoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advert
        fields = '__all__'
        extends = ("advert_id")

class AuthSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("email", "username", "password")

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = ("advert_id", "image")
    
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = '__all__'

