from django.urls import path

from model_basic import views

app_name = 'model'
urlpatterns = [
    path('', views.list_person, name="list"),
    path('create', views.create_person, name="create"),
    path('update/<int:pk>', views.update_person, name='update'),
    path('delete/<int:pk>', views.delete_person, name='delete'),
    path('save/<int:pk>', views.save_person, name='save'),
    path('save/', views.save_person, name='save'),

]
