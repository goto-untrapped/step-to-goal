from django.http import HttpResponse
from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render,redirect
from django.template.context_processors import debug, request
from .forms import GoalForm
from .forms import ListForm
from .models import Goal
from rest_framework import generics,status
from .serializers import GoalSerializer, TodoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


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
	form = GoalSerializer()
	return render(request, 'index.html',{   #index.htmlにつながる
		'form':form,
	})


@api_view(['POST'])
def create_goals(request):		#目標の入力を処理するためのビュー
	print("create_goalsビューを実行しました")
	goal_serializer = GoalSerializer(data=request.data)
	#if request.method == 'POST':
	if goal_serializer.is_valid():
		#form = ListForm(request.POST)
		#print("POSTを実行しました")
		#if form.is_valid():
		#print("Is_validを実行しました")
		goal_serializer.save()			#フォームのデータをデータベースに保存できる
		return Response(goal_serializer.data, status=status.HTTP_201_CREATED)		# 保存後にリダイレクト
	return Response(goal_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	""" else:
		form = ListForm()
		print("elseを実行しました") """
		
	goals = Goal.objects.all()
	return render(request, 'goal_input.html', {'goals':goals, 'form':form})
	
#データベースからすべての目標を取得し、それらを goal_data.html テンプレートに渡してレンダリング

@api_view(['GET'])
def list_goals(request):		# 目標のリストを表示するためのビュー
    print("list_goalsビューを実行しました")
    goals = Goal.objects.all()		#データベースから目標のリストが取得
    list_serializer = GoalSerializer(goals, many=True)
    #return render(request, 'goal_data.html', {'goals': goals})
    return Response(list_serializer.data)


def update(request):
	if request.method == 'POST':
		form = ListForm(request.POST)
		if form.is_valid():
			form.save()		# フォームのデータを保存
			return redirect('goal_data')
		else:
			form = ListForm()

			return render(request, 'index.jsx',{'form':form})
			subject = form.cleaned_data['subject']
			description = form.cleaned_data['description']
			goal = Goal.objects.create(subject=subject, description=description)
			return redirect(goal_data)
		
class GoalListCreateAPIView(generics.ListCreateAPIView):
    queryset = Goal.objects.all()  # モデルのクエリセットを取得します
    serializer_class = GoalSerializer  # シリアライザークラスを指定します

#GETリクエストで目標のリストを取得し、POSTリクエストで新しい目標を作成するAPIビューとして機能
	

