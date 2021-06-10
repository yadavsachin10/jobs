from django.db import models

STATUS = (
    ('None','None'),
    ('Active','Active'),
    ('Closed','Closed'),
)

JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
    ('Internship','Internship'),
)

class Job(models.Model):
    title = models.CharField(max_length=36)
    desc = models.TextField(max_length=320)
    location = models.CharField(max_length=20)
    pay_range = models.CharField(max_length=16,null=True)
    status = models.CharField(max_length=6, choices=STATUS, default='None')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

class JobApplication(models.Model):
    full_name = models.CharField(max_length=36, null=True, blank=True)
    city = models.CharField(max_length=18, null=True, blank=True)
    resume = models.FileField(upload_to='resume',null=True,blank=True)
    graduation_year = models.IntegerField(blank=True)
    job_type = models.CharField(max_length=30, choices=JOB_TYPE, default='Full Time', null=True)

    def __str__(self):
        return f"Application of {self.full_name}"




