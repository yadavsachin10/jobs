from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.generic import ListView, DetailView, FormView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from .models import Job, JobApplication
from .serializers import JobSerializer, JobAppSerializer
from .forms import applyForm

@api_view(['GET','POST'])
def job_list(request):
    if request.method == 'GET':
        job_object = Job.objects.all()
        serializer = JobSerializer(job_object,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = JobSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def job_detail(request,pk):
    try:
        job = Job.objects.get(pk=pk)
    except Job.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer=JobSerializer(job)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer=JobSerializer(job,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        job.delete()
        return Respose(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def applied_list(request):
    if request.method == 'GET':
        job_object = JobApplication.objects.all()
        serializer = JobAppSerializer(job_object,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = JobAppSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def applied_user_detail(request,pk):
    try:
        job = JobApplication.objects.get(pk=pk)
    except JobApplication.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer=JobAppSerializer(job)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer=JobAppSerializer(job,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        job.delete()
        return Respose(status=status.HTTP_204_NO_CONTENT)

class Jobs(ListView):
    model = Job
    template_name = 'job_details/home.html'

class JobDetail(DetailView):
    model = Job
    template_name = 'job_details/detail.html'

class ApplyPage(FormView):
    template_name = 'job_deatil/apply_page.html'
    form = applyForm()
    success_url = 'jobs/'
    
