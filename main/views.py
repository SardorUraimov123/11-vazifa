from django.shortcuts import render
from . import models

def home(request):
    trending_news = []
    weekly_news = []
    recent_news = models.Post.objects.all()[0:5]
    categories = models.Category.objects.all()[0:5]
    news_dict = dict()
    for category in categories:
        news = models.Post.objects.filter(category=category)
        news_dict[category.name] = news
    context = {
        'trending_news': trending_news, 
        'weekly_news': weekly_news, 
        'recent_news': recent_news,
        'categories': categories,
        'news_dict': news_dict
        }
    return render(request,'front/index.html',context)

def about(request):
    return render(request,'front/about.html')

def contact(request):
    return render(request,'front/contact.html')

def news(request):
    posts = models.Post.objects.all()
    categories = models.Category.objects.all()
    recent_news = models.Post.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
        'recent_news':recent_news,
        }
    return render(request,'front/news.html',context)

def detail_news(request,id):
    post = models.Post.objects.get(id=id)
    context = {'post': post}
    return render(request,'front/details.html',context)