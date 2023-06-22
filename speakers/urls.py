from django.urls import path
from speakers import views
urlpatterns = [
    path('', views.speaker_list, name='conference'),
    path('create/', views.create_speaker, name='create_a_new_speaker'),
    path('<int:speaker_id>/', views.read_speaker, name='view_single_speaker'),
    path('<int:speaker_id>/update', views.update_speaker, name='update_speaker'),
    path('<int:speaker_id>/delete', views.delete_speaker, name='delete_speaker'),
]

