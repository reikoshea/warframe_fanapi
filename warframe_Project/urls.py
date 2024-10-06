from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles import views
from django.urls import include, path, re_path

urlpatterns = [
    path('', include("warframe_site.urls")),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r"^static/(?P<path>.*)$", views.serve),
    ]
