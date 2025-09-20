from rest_framework import serializers
from ..models import *


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    # is_liked = serializers.SerializerMethodField()
    # is_saved = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    # def get_is_liked(self, obj):
    #     user = self.context["request"].user
    #     return user.is_authenticated and user in obj.liked_by.all()

    # def get_is_saved(self, obj):
    #     user = self.context["request"].user
    #     return user.is_authenticated and user in obj.saved_by.all()

class BookCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class BorrowerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Borrower
        fields = '__all__'

