from django.shortcuts import render
from rest_framework import viewsets,mixins
from .import models
from .import serializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import views, status,filters,pagination
from rest_framework.response import Response
# Create your views here.

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

class ArticlePagination(pagination.PageNumberPagination):
    page_size=5
    page_size_query_param=page_size
    max_page_size=100

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class=ArticlePagination
    search_fields = ['headline','category']

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer








# class ArticleCreateView(viewsets.ModelViewSet):
#     queryset = models.Article.objects.all()
#     serializer_class = serializers.ArticleSerializer

#     def create(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# class ReviewCreateViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin):
#     queryset = models.Review.objects.all()
#     serializer_class = serializers.ReviewSerializer

#     def create(self, request, pk):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(article=models.Article.objects.get(pk=pk), reviewer=request.user)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    


# class UpdateArticleView(generics.UpdateAPIView):
#     queryset = models.Article.objects.all()
#     serializer_class = serializers.ArticleSerializer

#     def put(self, request, pk):
#         article = self.get_object()
#         serializer = self.get_serializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)