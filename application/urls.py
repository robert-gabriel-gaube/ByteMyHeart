from django.urls import path

from application import views


urlpatterns = [
    path('interestform', views.BigRegisterFormView.as_view()),
    path('register', views.UserRegisterFormView.as_view()),
    path('reports', views.ReportsView.as_view()),
    path('reports/action/<int:pk>/<username>/<int:status>', views.ReportsActionView.as_view()),
    path('report/<int:pk>', views.ReportView.as_view()),
    path('create-report/', views.CreateReportView.as_view()),
    path('user-main-page', views.UserMainPageView.as_view()),
    path('', views.IndexPageView.as_view()),
]
