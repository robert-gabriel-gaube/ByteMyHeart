from django.urls import path

from application import views


urlpatterns = [
    path('interestform', views.BigRegisterFormView.as_view()),
    path('register', views.UserRegisterFormView.as_view()),
    path('reports', views.ReportsView.as_view())
    
]
