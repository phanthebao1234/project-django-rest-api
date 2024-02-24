from rest_framework import generics
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Blog
from .serializer import BlogSerializer

class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    def perform_create(self, serializer):
        serializer.save()
        title = serializer.validated_data_get('title')
        content = serializer.validated_data_get('content')
        
        if content is None:
            content = title
        serializer.save(content = content)

blog_list_create_view = BlogListCreateAPIView.as_view()
    
