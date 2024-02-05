from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.AboutMeView.as_view({'get': 'about_me'})),

    path('blogs/', views.BlogListView.as_view({'get': 'blogs'})),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view({'get': 'blog_item'})),

    path('social/', views.SocialView.as_view({'get': 'social'})),
    path('experiments/', views.ExperienceListView.as_view({'get': 'experience'})),
    path('projects/', views.ProjectListView.as_view({'get': 'projects'})),
    path('contact/', views.ContactCreateView.as_view({'post': 'create'}))
]
