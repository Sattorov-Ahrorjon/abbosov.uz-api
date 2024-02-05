from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.static import serve
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Abbosov Blog APIv1",
        default_version='v1',
        description="API for project Abbosov Blog",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="sattorov.ahu@gmail.com", name="sattorov.ahu@gmail.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/', include('api.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    re_path(r'static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
