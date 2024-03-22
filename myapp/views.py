from imaplib import _Authenticator
import sqlite3
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render,redirect
from django.template.context_processors import debug, request
from .forms import GoalForm
from .models import Goal, TestTarget, TestTodo, User0322
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
		
@api_view(['POST'])
def login_view(request):
    # username = request.data.get('username')
    # password = request.data.get('password')
    # # user = authenticate(username=username, password=password)
	
    # dbFile = 'myapp_user.db'
    # con = sqlite3.connect(dbFile)
    # cur = con.cursor()
    # cur.execute('SELECT * FROM myapp_user')
    # for row in cur:
    #     if row[username] == username:
    #         return JsonResponse({'message': 'Login successful'})
    # return JsonResponse({'message': 'User does not exist'}, status=400)

    try:
        # ユーザーを検索して認証する
        user = User0322.objects.get(username=username)
        print(user.username)
        if user:
            return JsonResponse({'message': 'Login successful'})
		# if user.check_password(password):
		# if user:
            # パスワードが一致した場合の処理
            return JsonResponse({'message': 'Login successful'})
        else:
            # パスワードが一致しない場合の処理
            return JsonResponse({'message': 'Invalid credentials'}, status=400)
    except User.DoesNotExist:
        # ユーザーが存在しない場合の処理
        return JsonResponse({'message': 'User does not exist'}, status=400)

    # if user is not None:
    #     # ユーザーが存在する場合の処理
    #     return Response({'message': 'Login successful'})
    # else:
    #     # ユーザーが存在しない場合の処理
    #     return Response({'message': 'Invalid credentials'}, status=400)
	

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

	print("backend:", len(target_data))
	return JsonResponse({'targets': target_data})
