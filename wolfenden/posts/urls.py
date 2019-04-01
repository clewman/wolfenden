from django.urls import path

from .views import UrbanPageView, NaturePageView, PortraitPageView

app_name = 'posts'
urlpatterns = [
    path('urban', UrbanPageView.as_view(), name='urban'),
    path('nature', NaturePageView.as_view(), name='nature'),
    path('portrait', PortraitPageView.as_view(), name='portrait'),
]
