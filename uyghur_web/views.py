from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'Main_page.html')

def suggestion(request):
    return render(request, 'suggestions.html')


def create_suggestion(request):
	print request.POST
	return HttpResponse("cool")

