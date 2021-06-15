from django.urls import path
from .views import Jobs,JobDetail,job_list,job_detail,applied_list,applied_user_detail

app_name = 'jobs'

urlpatterns = [
    path('',Jobs.as_view()),
    path('<pk>',JobDetail.as_view(),name='detail'),
    path('jobs/',job_list),
    path('jobs/<int:pk>',job_detail),
    path('applied/',applied_list),
    path('applied/<int:pk>',applied_user_detail),
]