from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import AboutMe, Blog, BlogImage, Social, Experience, Project, Contact


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'start_date', 'end_date',)
    list_display_links = ('name',)
    readonly_fields = ('get_image',)

    fieldsets = (
        (None, {'fields': (('name', 'description'),)}),
        (None, {'fields': (('position', 'image', 'get_image'),)}),
        (None, {'fields': (('start_date', 'end_date'),)}),
        (None, {'fields': (('project_url', 'github'),)})
    )

    def get_image(self, obj):
        return mark_safe(
            f"<img src='{obj.image.url}' width='70px' height='80px' />")
    get_image.short_description = ''


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'start_date', 'end_date')
    list_display_links = ('name',)

    fieldsets = (
        (None, {'fields': (('name', 'position'),)}),
        (None, {'fields': (('start_date', 'end_date'),)}),
        ("About Company", {'fields': ('company_url', 'description')})
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject', 'email')
    list_display_links = ('name',)
    list_filter = ('subject',)
    fieldsets = (
        (None, {'fields': (('name', 'email'),)}),
        (None, {'fields': (('subject', 'message'),)})
    )


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'lang')
    list_display_links = ('name',)

    fieldsets = (
        (None, {'fields': (('name', 'phone'),)}),
        (None, {'fields': (('email', 'lang'),)})
    )


class BlogImageTabular(admin.TabularInline):
    model = BlogImage
    readonly_fields = ('get_image',)
    fieldsets = (
        (None, {'fields': ('image', 'get_image')}),
    )
    extra = 1

    def get_image(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' width='60px' height='70px' />")


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'theme', 'description')
    list_display_links = ('title',)
    inlines = [BlogImageTabular]
    fieldsets = (
        (None, {'fields': (('title', 'theme',),)}),
        (None, {'fields': ('description',)})
    )


# @admin.register(BlogImage)
# class BlogImageAdmin(admin.ModelAdmin):
#     list_display = ('id', 'get_image')
#     list_display_links = ('id', 'get_image')
#
#     def get_image(self, obj):
#         return mark_safe(f"<img src='{obj.image.url}' width='30px' height='40px' />")


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_telegram', 'get_github', 'get_linkedin', 'get_instagram', 'get_facebook', 'get_twitter')
    list_display_links = (
        'id', 'get_telegram', 'get_github', 'get_linkedin', 'get_instagram', 'get_facebook', 'get_twitter'
    )

    readonly_fields = ('get_telegram',)

    fieldsets = (
        (None, {'fields': (('linkedin', 'github', 'telegram'),)}),
        (None, {'fields': (('facebook', 'twitter', 'instagram'),)})
    )

    def get_telegram(self, obj):
        return mark_safe(
            f"<img src='https://www.svgrepo.com/show/504946/telegram.svg'"
            f"width='30px' height='30px' />")

    def get_github(self, obj):
        return mark_safe(
            f"<img src='https://www.svgrepo.com/show/521688/github.svg'"
            f"width='30px' height='30px' />")

    def get_linkedin(self, obj):
        return mark_safe(
            f"<img src='https://www.svgrepo.com/show/521725/linkedin.svg'"
            f"width='30px' height='30px' />")

    def get_instagram(self, obj):
        return mark_safe(
            f"<img src='https://www.svgrepo.com/show/521711/instagram.svg'"
            f"width='30px' height='30px' />")

    def get_facebook(self, obj):
        return mark_safe(
            f"<img src='https://www.svgrepo.com/show/521654/facebook.svg'"
            f"width='30px' height='30px' />")

    def get_twitter(self, obj):
        return mark_safe(
            f"<img src='https://www.svgrepo.com/show/510291/twitter.svg'"
            f"width='30px' height='30px' />")

    get_telegram.short_description = "Telegram"
    get_github.short_description = "Github"
    get_linkedin.short_description = "Linkedin"
    get_instagram.short_description = "Instagram"
    get_facebook.short_description = "Facebook"
    get_twitter.short_description = "Twitter"


admin.site.site_header = "Administration"
admin.site.index_title = "Abbosov Muhammadamin"
admin.site.site_title = "Blog"
