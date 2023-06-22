from django.urls import path
from speakers import views
urlpatterns = [
    path('', views.speaker_list),
    path('create/', views.create_speaker),
    path('<int:speaker_id>/', views.read_speaker),
    path('<int:speaker_id>/update', views.update_speaker),
    path('<int:speaker_id>/delete', views.delete_speaker),
]

