from django.urls import path
from .views import index,foo,hello,goal_data,form, login_view,update
from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
    path('login/', views.login_view, name='login'),
]