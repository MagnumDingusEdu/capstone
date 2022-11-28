from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path("", include("website.urls", namespace="website")),
    path("", include("accounts.urls")),

    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path('accounts/', include('allauth.urls')),
    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
