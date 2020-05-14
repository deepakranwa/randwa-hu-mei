from django.http import HttpResponse
from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required    # its  a decorator.. see other decoratos on google
# just add above definition of functions whose view req. login.. argument is .. where to redirect if ! logged in 
def article_list(request):
    articles = Article.objects.all().order_by('date');
    return render(request, 'articles/article_list.html', { 'articles': articles })

def article_detail(request, slug):
    deets=Article.objects.get(slug=slug)
    return render(request, 'articles/article_detailed.html',{'slug_art':deets})


@login_required(login_url="/accounts/login/")
def create_article(request):
    return render(request,'create_article.html')