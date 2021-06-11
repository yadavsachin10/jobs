from django.urls import path
from .views import jobs,job_list,job_detail,applied_list,applied_user_detail

app_name = 'jobs'

urlpatterns = [
    path('',jobs.as_view()),
    # path('jobs/',job_list),
    path('jobs/<int:pk>',job_detail,name='detail'),
    path('applied/',applied_list),
    path('applied/<int:pk>',applied_user_detail),
]
