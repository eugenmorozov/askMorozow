from django.shortcuts import render

from django.views.generic import TemplateView
from django.http import HttpResponse
# Create your views here.
class AboutView(TemplateView):
	template_name = 'about.html'
def logged_out_view(request):
	return render(request, 'logged_out.html')
def index(request):
	return render(request, 'question_form.html')
def registration(request):
	return render(request, 'registration.html')
def login(request):
	return render(request,'login.html')
def settings(request):
	return render(request,'settings.html')
def ask(request):
	return render(request,'ask.html')
def question(request):	
	return render(request,'question.html')
