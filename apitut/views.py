from django.http import JsonResponse
from .models import BlogPosts
from .serializers import BlogPostSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from apitut import serializers


@api_view(["GET", "POST"])
def post_list(request, format=None):
    if request.method == "GET":
        posts = BlogPosts.objects.all()
        post_title = request.query_params.get("title")

        if post_title:
            posts = posts.filter(title=post_title)

        serializer = BlogPostSerializers(posts, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = BlogPostSerializers(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "POST", "DELETE"])
def post_detail(request, pk, format=None):
    try:
        post = BlogPosts.objects.get(id=pk)
    except BlogPosts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND )

    if request.method == "GET":
        serializer = BlogPostSerializers(post)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = BlogPostSerializers(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)