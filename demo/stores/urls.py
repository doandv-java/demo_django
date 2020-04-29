from django.urls import path

from . import views

app_name = "stores"
urlpatterns = [
    path('', views.IndexViewStore.as_view(), name="index"),
    path('', views.update, name='update'),
]
