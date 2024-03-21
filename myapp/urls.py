from django.urls import path
from .views import index,foo,hello,goal_data,goal_input,form,update
from . import views
from .forms import ListForm

urlpatterns = [
	path('',views.index, name = 'index'),
	path('foo', views.foo, name = 'foo'),
	path('hello', views.hello, name = 'hello'),
    path('form', views.form, name = 'form'),
    path('input/', views.update, name='input'), #？？
    path('goals/', views.goal_data, name='goal_data'),
    path('goalInput/', views.goal_input, name = 'goal_input'),
]