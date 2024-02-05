from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import (
    Blog,
    Social,
    AboutMe,
    Project,
    Contact,
    Experience,
)
from api.serializers import (
    BlogSerializer,
    SocialSerializer,
    ProjectSerializer,
    AboutMeSerializer,
    ExperienceSerializer,
    ContactSerializer
)

from drf_yasg.utils import swagger_auto_schema


class AboutMeView(ViewSet):
    @swagger_auto_schema(
        operation_description="About me",
        responses={200: AboutMeSerializer()},
        tags=['AboutMe']
    )
    def about_me(self, request):
        values = AboutMe.objects.first()
        if values is None:
            return Response(data={'about_me': ""}, status=status.HTTP_404_NOT_FOUND)
        return Response(
            data={'about_me': AboutMeSerializer(values, context={'request': request}).data}, status=status.HTTP_200_OK)


# class AboutMeView(APIView):
#     def get(self, request):
#         about_me = AboutMe.objects.first()
#         serializer = AboutMeSerializer(about_me, context={'request': request}).data
#         return Response(data={'about_me': serializer}, status=status.HTTP_200_OK)


class BlogListView(ViewSet):
    @swagger_auto_schema(
        operation_description="Blogs list",
        responses={200: BlogSerializer()},
        tags=['Blogs']
    )
    def blogs(self, request):
        blogs = Blog.objects.all()
        if blogs is None:
            return Response(data={'blogs': ""}, status=status.HTTP_404_NOT_FOUND)

        return Response(
            data={'blogs': BlogSerializer(blogs, context={'request': request}, many=True).data},
            status=status.HTTP_200_OK
        )


# class BlogListView(APIView):
#     def get(self, request):
#         blogs = Blog.objects.all()
#         serializer = BlogSerializer(blogs, context={'request': request}, many=True).data
#         return Response(data={"blogs": serializer}, status=status.HTTP_200_OK)


class BlogDetailView(ViewSet):
    @swagger_auto_schema(
        operation_description="Blog item",
        responses={200: BlogSerializer()},
        tags=["Blog item"]
    )
    def blog_item(self, request, pk):
        blog = Blog.objects.filter(id=pk).first()
        if blog is None:
            return Response(data={'blog': ""}, status=status.HTTP_404_NOT_FOUND)

        return Response(
            data={'blog': BlogSerializer(blog, context={'request': request}).data}, status=status.HTTP_200_OK)


# class BlogDetailView(APIView):
#     def get(self, request, pk):
#         blog = Blog.objects.filter(id=pk).first()
#         serializer = BlogSerializer(blog, context={'request': request}).data
#         return Response(data={"blog": serializer}, status=status.HTTP_200_OK)


class SocialView(ViewSet):
    @swagger_auto_schema(
        operation_description="Social list",
        responses={200: SocialSerializer()},
        tags=["Social list"]
    )
    def social(self, request):
        social = Social.objects.first()
        if social is None:
            return Response(data={'social': ""}, status=status.HTTP_404_NOT_FOUND)

        return Response(
            data={'social': SocialSerializer(social, context={'request': request}).data}, status=status.HTTP_200_OK)


# class SocialView(APIView):
#     def get(self, request):
#         social = Social.objects.first()
#         serializer = SocialSerializer(social, context={'request': request}).data
#         return Response(data={"social": serializer}, status=status.HTTP_200_OK)


class ExperienceListView(ViewSet):
    @swagger_auto_schema(
        operation_description="Experience list",
        responses={200: ExperienceSerializer()},
        tags=["Experience list"]
    )
    def experience(self, request):
        experience = Experience.objects.all()
        if experience is None:
            return Response(data={'experience': ""}, status=status.HTTP_404_NOT_FOUND)

        return Response(
            data={'experience': ExperienceSerializer(experience, context={'request': request}, many=True).data},
            status=status.HTTP_200_OK
        )


# class ExperienceListView(APIView):
#     def get(self, request):
#         experiments = Experience.objects.all()
#         serializer = ExperienceSerializer(experiments, many=True, context={'request': request}).data
#         return Response(data={'experience': serializer}, status=status.HTTP_200_OK)


class ProjectListView(ViewSet):
    @swagger_auto_schema(
        operation_description="Project list",
        responses={200: ProjectSerializer()},
        tags=["Project list"]
    )
    def projects(self, request):
        projects = Project.objects.all()
        if projects is None:
            return Response(data={'projects': ""}, status=status.HTTP_404_NOT_FOUND)

        return Response(
            data=ProjectSerializer(projects, context={'request': request}, many=True), status=status.HTTP_200_OK)


# class ProjectListView(APIView):
#     def get(self, request):
#         projects = Project.objects.all()
#         serializer = ProjectSerializer(projects, many=True, context={'request': request}).data
#         return Response(data={'projects': serializer}, status=status.HTTP_200_OK)


class ContactCreateView(ViewSet):
    @swagger_auto_schema(
        operation_description="Contact create",
        responses={201: ContactSerializer()},
        tags=["Contact"],
        request_body=ContactSerializer
    )
    def create(self, request):
        data = request.data
        serializer = ContactSerializer(data=data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_204_NO_CONTENT)

        Contact(
            name=data.get('name'), email=data.get('email'), subject=data.get('subject'), message=data.get('message')
        ).save()
        return Response(status=status.HTTP_201_CREATED)

# class ContactCreateView(APIView):
#     def post(self, request):
#         serializer = ContactSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
