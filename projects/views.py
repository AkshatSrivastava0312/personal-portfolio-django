from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from about.models import SocialLink
# Create your views here.
def show(request):
    project_object = Project.objects.all()
    social_obj = SocialLink.objects.all()[0]
    param = {'project':project_object,'social_data':social_obj}
    return render(request,'projects.html',param)
    