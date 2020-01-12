from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Article

def homepage(request):
    #return HttpResponse('after all this time i\'m coming home to you')
    return render(request, "homepage.html")
def about(request ):
    #return HttpResponse('Kaboum')
    return render(request,  "about.html")
