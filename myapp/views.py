from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render,redirect
from django.template.context_processors import debug, request
from .forms import GoalForm
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