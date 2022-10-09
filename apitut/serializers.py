from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import BlogPosts

class BlogPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogPosts
        fields = ["name", "post"]