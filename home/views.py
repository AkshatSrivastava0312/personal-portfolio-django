from django.shortcuts import render
from django.http import HttpResponse
from .models import Tagline,TopSkills,ImageGallery
from about.models import SocialLink
# Create your views here.
def show(request):
    social_obj = SocialLink.objects.all()[0]
    t_data = Tagline.objects.all()[0]
    t_skills = TopSkills.objects.all()[0]
    img_data = ImageGallery.objects.all()
    tag_data = {'tag_data':t_data,'top_skills':t_skills,'image_data':img_data,'social_data':social_obj}
    return render(request, 'home.html',tag_data)