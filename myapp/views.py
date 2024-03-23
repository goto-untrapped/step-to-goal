from imaplib import _Authenticator
import json
import sqlite3
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render,redirect
from django.template.context_processors import debug, request
from .forms import GoalForm
from .models import Goal, TestTarget, TestTodo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.middleware.csrf import get_token
from myapp.models import User

# Create your views here.

def index(request):
	# html = "<h1>myappのウェルカムページです</h1>"
	# return HttpResponse(html) 
	return render(request,'index.html')

def foo(request):
	html = "<h1>fooが指定されたときのページです</h1>"
	return HttpResponse(html)

def hello(request):
	#form = GoalForm()
	return render(request,'index.html')

def form(request):
	form = GoalForm()
	return render(request, 'index.html',{   #index.htmlにつながる
		'form':form,
	})

def goal_data(request):
	goals = Goal.objects.all()
	form = GoalForm(request.POST or None)
	if request.method == 'POST':
		form = GoalForm(request.POST)
		if form. is_valid():
			goals = Goal()
			form.save()
			return redirect('goal_data')
	return render(request, 'index.html', {'goals':goals, 'form':form})
	
	ctx = {"form": form}
	if form. is_valid():
		YourGoal = form.cleaned_data["forms"]
		obj = GoalForm(YourGoal=form)
		obj.save()
	return render(request,'index.html',ctx)
	#goal_list = 

def update(request):
	if request.method == 'POST':
		form = GoalForm(request.POST)
		if form.is_valid():
			form.save()
			if form. is_valid():
				form.save()
				return redirect('goal_data')
			else:
				form = GoalForm()

			return render(request, 'index.html',{'form':form})
			subject = form.cleaned_data['subject']
			description = form.cleaned_data['description']
			goal = Goal.objects.create(subject=subject, description=description)
			return redirect(goal_data)

def userSaveView(request):
	data = json.loads(request.body)
	username = data["username"]
	password = data["password"]
	global numbering_user_id
	# データベースに保存する処理
	User.objects.create(username=username, password=password)

	return JsonResponse({'message': 'success'})

def loginView(request):
	data = json.loads(request.body)
	username = data["username"]
	password = data["password"]
	try:
		user = User.objects.get(username=username)
		if user:
			if password == user.password:
				return JsonResponse({'message': 'Login successful'})
			else:
				return JsonResponse({'message': 'Wrong password'}, status=400)
	except:
		return JsonResponse({'message': 'User does not exist'}, status=400)

def CsrfView(request):
    return JsonResponse({'token': get_token(request)})

def PingView(request):
    return JsonResponse({'result': True})

def targetView(request):
	targets = TestTarget.objects.all()
	target_todo_dict = {}
	for target in targets:
		target_todo_dict[target.target_id] = []
	
	todos = TestTodo.objects.all()
	for target in targets:
		for todo in todos:
			if target.target_id == todo.target_id:
				target_todo_dict[target.target_id].append(todo)
				continue	

	target_data = []
	for target in targets:
		target_dict = {
            'target_id': target.target_id,
            'user_id': target.user_id,
            'content': target.content,
			'todos': [
				{
					'todo_id': todo.todo_id,
					'content': todo.content,
				}
				for todo in target_todo_dict[target.target_id]
			]
        }
		target_data.append(target_dict)

	return JsonResponse({'targets': target_data})

def myTargetView(request):
	# params = json.loads(request.body)
	# username = params.get('username', None)
	username = ''
	print(request)
	print(request.GET)
	if 'username' in request.GET:
		print('in')
		username = request.GET.get('username')
	print(username)

	targets = TestTarget.objects.filter(user_id=username)
	# targets = TestTarget.objects.all()
	# target_todo_dict = {}
	# for target in targets:
	# 	target_todo_dict[target.target_id] = []
	
	# todos = TestTodo.objects.all()
	# for target in targets:
	# 	for todo in todos:
	# 		if target.target_id == todo.target_id:
	# 			target_todo_dict[target.target_id].append(todo)
	# 			continue

	target_data = []
	for target in targets:
		target_dict = {
            'target_id': target.target_id,
            'user_id': target.user_id,
            'content': target.content,
			'todos': [
				{
					# 'todo_id': todo.todo_id,
					'todo_id': "a",
					# 'content': todo.content,
					'content': "b",
				}
				# for todo in target_todo_dict[target.target_id]
			]
        }
		target_data.append(target_dict)

	return JsonResponse({'targets': target_data})


numbering_target_id = 0
numbering_todo_id = 0
def registerView(request):
	data = json.loads(request.body)
	content = data["target"]
	todos = data["todos"]
	username=data["username"]
	global numbering_target_id
	global numbering_todo_id
	# データベースに保存する処理
	TestTarget.objects.create(target_id = numbering_target_id, user_id=username, content=content)

	for todo in todos:
		if todo:
			TestTodo.objects.create(todo_id=numbering_todo_id ,target_id=numbering_target_id, content=todo["text"])
			numbering_todo_id += 1
	numbering_target_id += 1
	return JsonResponse({'message': 'success'})

