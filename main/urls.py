from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('news/',views.news, name='news'),
    path('detail-news/<int:id>',views.detail_news, name='detail-news')
]
