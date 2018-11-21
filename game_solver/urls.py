from django.urls import path
from . import views

app_name = 'game_solver'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail')
]
