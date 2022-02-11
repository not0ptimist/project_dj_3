''' news urls

'''
from django.urls import path
from . import views


urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create/', views.create_news, name='create_news'),
    # https://docs.djangoproject.com/en/4.0/intro/tutorial03/#writing-more-views
    # про <>, не забываем про удаленные страницы, из-за которых нет id
    path('<int:pk>', views.UserNewsDetailView.as_view(), name='user-news-detail'),
    path('<int:pk>/edit', views.UserNewsEditView.as_view(), name='user-news-edit'),
    path('<int:pk>/delete', views.UserNewsDeleteView.as_view(), name='user-news-delete'),
]