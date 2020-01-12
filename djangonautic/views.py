from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Article

def homepage(request):
    #return HttpResponse('after all this time i\'m coming home to you')
    last3art = Article.objects.all().order_by('-id')[:3]

    return render(request, "homepage.html",{'last3art': last3art})
def about(request ):
    #return HttpResponse('Kaboum')
    return render(request,  "about.html")
