from django.forms import ModelForm
from .models import JobApplication

class ApplyForm(ModelForm):
    class Meta:
        model = JobApplication
        fields = ['full_name','city','resume','graduation_year','job_type',]