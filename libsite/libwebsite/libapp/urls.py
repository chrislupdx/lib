from django.urls import path
from . import views

app_name = 'libapp' # for namespacing
urlpatterns = [
    path('', views.index, name='index')
]