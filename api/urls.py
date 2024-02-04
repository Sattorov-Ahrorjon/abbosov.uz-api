from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.AboutMeView.as_view()),
    path('blog/', views.BlogView.as_view()),
    path('social/', views.SocialView.as_view()),
    path('experience/', views.ExperienceListView.as_view()),
    path('projects/', views.ProjectListView.as_view())
]
