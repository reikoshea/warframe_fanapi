from django.urls import path

from .views import warframes

urlpatterns = [
    path("warframes/", warframes.index, name="index"),
    path("warframes/<str:warframe_name>/", warframes.by_name, name="by_name"),
]
