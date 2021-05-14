from django.urls import path
from . import views

urlpatterns = [
    path('',views.blog_list,name='blog_list'),
    path('recent/',views.recent,name='recent'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('profile/<username>/',views.user_profile,name='profile'),
]
