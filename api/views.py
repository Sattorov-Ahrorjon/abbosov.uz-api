from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (
    Blog,
    Social,
    AboutMe,
    Project,
    Experience
)
from api.serializers import (
    BlogSerializer,
    SocialSerializer,
    ProjectSerializer,
    AboutMeSerializer,
    ExperienceSerializer
)


class AboutMeView(APIView):
    def get(self, request):
        about_me = AboutMe.objects.first()
        serializer = AboutMeSerializer(about_me, context={'request': request}).data
        return Response(data={'about_me': serializer}, status=status.HTTP_200_OK)


class BlogListView(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, context={'request': request}, many=True).data
        return Response(data={"blogs": serializer}, status=status.HTTP_200_OK)


class BlogDetailView(APIView):
    def get(self, request, pk):
        blog = Blog.objects.filter(id=pk).first()
        serializer = BlogSerializer(blog, context={'request': request}).data
        return Response(data={"blog": serializer}, status=status.HTTP_200_OK)


class SocialView(APIView):
    def get(self, request):
        social = Social.objects.first()
        serializer = SocialSerializer(social, context={'request': request}).data
        return Response(data={"social": serializer}, status=status.HTTP_200_OK)


class ExperienceListView(APIView):
    def get(self, request):
        experiments = Experience.objects.all()
        serializer = ExperienceSerializer(experiments, many=True, context={'request': request}).data
        return Response(data={'experience': serializer}, status=status.HTTP_200_OK)


class ProjectListView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True, context={'request': request}).data
        return Response(data={'projects': serializer}, status=status.HTTP_200_OK)
