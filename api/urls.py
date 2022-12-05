from django.urls import path
from . import views

urlpatterns = [
    path('users/<int:user_id>', get_user),
    path('jobs/<int:job_id>', get_job),
    path('jobs/', create_job),
    path('jobs/<int:job_id>', update_job),
    path('jobs/<int:job_id>', delete_job),
]
