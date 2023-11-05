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
    path('login', views.LoginView.as_view()),
    path('matches/match/<username>' , views.ViewMatchView.as_view()),
    path('view-my-profile/' , views.ViewMyProfileView.as_view()),
    path('set-date-offer/<int:pk>/<status>', views.SetDateOfferView.as_view()), 
    path('edit-my-profile/', views.EditMyProfileView.as_view()),   
    path('set-date-offer/<int:pk>/<status>', views.SetDateOfferView.as_view()),    
    path('matches', views.MatchesView.as_view()),
    path('view-profile/<username>', views.ViewProfileView.as_view()),
    path('match', views.MatchView.as_view()),
    path('match-logic/<int:choice>', views.MatchLogicView.as_view()),
    path('blocked', views.BlockedView.as_view()),
    path('process-rating/<username>', views.ProcessRatingView.as_view())
]
