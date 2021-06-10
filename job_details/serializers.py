from rest_framework import serializers
from .models import Job, JobApplication

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id','title','desc','location','pay_range','status']

class JobAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ['id','full_name','city','job_type','graduation_year','resume']
