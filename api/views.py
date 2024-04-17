from main import models
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import serializers

@api_view(['GET'])
def get_category_list(request):
    queryset = models.Category.objects.all()
    category = serializers.CategorySerializer(queryset, many=True)
    return Response(category.data)


@api_view(['GET'])
def get_category_detail(request,id):
    queryset = models.Category.objects.get(id=id)
    post = serializers.CategorySerializer(queryset)
    return Response(post.data)


@api_view(['GET'])
def get_category_post_list(request,id):
    queryset = models.Post.objects.filter(category__id=id)
    post = serializers.PostSerializer(queryset, many=True)
    return Response(post.data)


@api_view(['GET'])
def get_post_list(request):
    queryset = models.Post.objects.all()
    post = serializers.PostSerializer(queryset, many=True)
    return Response(post.data)


@api_view(['GET'])
def get_post_detail(request,id):
    queryset = models.Post.objects.get(id=id)
    post = serializers.PostSerializer(queryset)
    return Response(post.data)