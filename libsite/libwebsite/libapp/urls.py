from django.urls import path
from . import views

app_name = 'libapp' # for namespacing
urlpatterns = [
# do you need a path specific to submitting content via submit button?
    path('', views.index, name='index'),
    path('check/<int:bookpk>/', views.checkinout, name='checkout'),
]

