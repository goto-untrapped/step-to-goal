from django.urls import path
from .views import index,foo,hello,list_goals,create_goals,form,update,GoalListCreateAPIView
from . import views
from .forms import ListForm

urlpatterns = [
	path('',views.index, name = 'index'),
	path('foo', views.foo, name = 'foo'),
	path('hello', views.hello, name = 'hello'),
    path('form', views.form, name = 'form'),
    path('input/', views.update, name='input'), #？？
    path('goals/', views.list_goals, name='goal_data'),
    path('goalInput/', views.create_goals, name = 'goal_input'),
    path('api/goals/', GoalListCreateAPIView.as_view(), name='goal-list-create')
]