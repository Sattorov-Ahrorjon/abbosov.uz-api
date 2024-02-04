from rest_framework import serializers
from .models import (
    Blog,
    Project,
    Experience,
    Contact,
    Social,
    AboutMe,
    BlogImage
)


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'image', 'description', 'position',
                  'start_date', 'end_date', 'project_url', 'github')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if instance.image and self.context:
            rep['image'] = self.context.get('request').build_absolute_uri(rep.get('image'))
        else:
            rep['image'] = None
        return rep


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('id', 'name', 'description', 'position', 'start_date',
                  'end_date', 'company_url')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'name', 'email', 'subject', 'message')


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ('id', 'telegram', 'github', 'linkedin', 'instagram', 'facebook', 'twitter',)


class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = ('id', 'name', 'location', 'email',
                  'phone', 'lang', 'cv_media')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if instance.cv_media and self.context:
            rep['cv_media'] = self.context.get('request').build_absolute_uri(rep.get('cv_media'))
        else:
            rep['cv_media'] = None
        return rep


class BlogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogImage
        fields = ('id', 'image')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if instance.image and self.context:
            rep['image'] = self.context.get('request').build_absolute_uri(rep.get("image"))
        else:
            rep['image'] = None
        return rep


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'description', 'theme')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['images'] = BlogImageSerializer(
            BlogImage.objects.filter(name=rep.get('id')), many=True, context=self.context).data
        return rep
