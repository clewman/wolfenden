from django.conf.urls import url
from . import views
from django.urls import include, path


app_name = 'den'
urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/urban/', views.urban, name='urban'),
    path('parallax/', views.parallax, name='parallax'),


]
