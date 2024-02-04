from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.AboutMeView.as_view()),

    path('blog/', views.BlogListView.as_view()),
    path('blog/<int:pk>/', views.BlogDetailView.as_view()),

    path('social/', views.SocialView.as_view()),
    path('experiments/', views.ExperienceListView.as_view()),
    path('projects/', views.ProjectListView.as_view())
]
