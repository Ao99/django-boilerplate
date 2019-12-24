from django.urls import path
from .views import CoreView

app_name='core'
urlpatterns = [
    path('', CoreView.as_view(), name='home'),
    path('about', CoreView.as_view(template_name='core/about.html'), name='about')
    ]