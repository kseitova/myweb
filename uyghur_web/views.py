from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'Main_page.html')

def event_form(request):
    return render(request, 'event_form.html')


def create_suggestion(request):
	print request.POST
	return HttpResponse("cool")

