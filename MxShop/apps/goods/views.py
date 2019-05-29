from django.shortcuts import render

# Create your views here.
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Goods
from .serializer import GoodsSerializer
from rest_framework import mixins
from rest_framework import filters, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filters import GoodsFilter
# class GoodsPagination(Page)


class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_class = GoodsFilter
    search_fields = ('name', 'goods_brief')
