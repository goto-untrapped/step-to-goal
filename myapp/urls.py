from django.urls import path
from .views import index,foo,hello,goal_data,form,update
from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
]