from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path("admin/", admin.site.urls),
    path("", include("nft.urls"),)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
