from django.http import HttpResponse
from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render,redirect
from django.template.context_processors import debug, request
from .forms import GoalForm
from .forms import ListForm
from .models import Goal


# Create your views here.

def index(request):
	html = "<h1>myappのウェルカムページです</h1>"
	return HttpResponse(html) 

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

def goal_input(request):		#目標の入力を処理するためのビュー
	print("goal_inputビューを実行しました")
	if request.method == 'POST':
		form = ListForm()
		print("POSTを実行しました")
		if form.is_valid():
			print("Is_validを実行しました")
			form.save()			#フォームのデータをデータベースに保存できる
			return redirect('goal_data')		# 保存後にリダイレクト
	else:
		form = ListForm()
		print("elseを実行しました")

	goals = Goal.objects.all()
	return render(request, 'goal_input.html', {'goals':goals, 'form':form})
	
#データベースからすべての目標を取得し、それらを goal_data.html テンプレートに渡してレンダリング


def goal_data(request):		# 目標のリストを表示するためのビュー
    print("goal_dataビューを実行しました")
    goals = Goal.objects.all()		#データベースから目標のリストが取得
    return render(request, 'goal_data.html', {'goals': goals})
	


def update(request):
	if request.method == 'POST':
		form = ListForm(request.POST)
		if form.is_valid():
			form.save()		# フォームのデータを保存
			return redirect('goal_data')
		else:
			form = ListForm()

			return render(request, 'index.html',{'form':form})
			subject = form.cleaned_data['subject']
			description = form.cleaned_data['description']
			goal = Goal.objects.create(subject=subject, description=description)
			return redirect(goal_data)