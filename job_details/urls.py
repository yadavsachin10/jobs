from django.urls import path
from .views import job_list,job_detail,applied_list,applied_user_detail

urlpatterns = [
    path('jobs/',job_list),
    path('jobs/<int:pk>',job_detail),
    path('applied/',applied_list),
    path('applied/<int:pk>',applied_user_detail),
]
