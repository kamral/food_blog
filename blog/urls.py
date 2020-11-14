from django.urls import path
from . import views


urlpatterns=[
    path('',views.Home.as_view(), name='home'),
    # данный url позволяет каждой записи относиться в свое1 категории
    # при нажатии на одну из категории
    path('category/<str:slug>/',views.PostByCategory.as_view(),name='category'),
    # вызываем конкретную статью
    path('tag/<str:slug>/', views.PostByTag.as_view(), name='tag'),

    path('post/<str:slug>/',views.GetPost.as_view(),name='post'),
    path('search/', views.Search.as_view(), name='search')

]