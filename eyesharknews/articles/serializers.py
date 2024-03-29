from rest_framework import serializers
from .models import BlogPosts

class BlogPostsSerializer(serializers.ModelSerializer):
    
    lookup_field = 'slug'

    class Meta:
        model = BlogPosts
        fields = '__all__'
