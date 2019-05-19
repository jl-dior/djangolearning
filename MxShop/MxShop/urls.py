"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include, path, re_path
import xadmin
from DjangoUeditor import urls as DjangoUeditor_urls
from MxShop.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static
from django.views.static import serve
from goods.views import GoodsListViewSet
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('goods', GoodsListViewSet)
# goods_list = GoodsListViewSet.as_view({
# 	'get': 'list'
# })
urlpatterns = [
	path('xadmin/', xadmin.site.urls),
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	path('docs', include_docs_urls(title="jl御用")),
	path('ueditor', include(DjangoUeditor_urls)),
	re_path('^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
