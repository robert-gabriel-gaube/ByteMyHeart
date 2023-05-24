from django.urls import path

from application import views


urlpatterns = [
    path('reports', views.ReportsView.as_view())
    
]
