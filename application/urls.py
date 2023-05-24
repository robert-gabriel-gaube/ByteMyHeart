from django.urls import path

from application import views


urlpatterns = [
    path('register', views.UserRegisterView.as_view()),
    path('reports', views.ReportsView.as_view())
    
]
