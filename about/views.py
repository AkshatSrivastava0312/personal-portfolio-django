from django.shortcuts import render
from django.http import HttpResponse
from .models import AboutImage,AboutText,CV,SocialLink

# Create your views here.
def show(request):
    social_obj = SocialLink.objects.all()[0]
    image_obj = AboutImage.objects.all()[0]
    text_obj = AboutText.objects.all()[0]
    cv_obj = CV.objects.all()[0]
    param = {'image':image_obj,'text':text_obj,'cv':cv_obj,'social_data':social_obj}
    return render(request,'about.html',param)
    