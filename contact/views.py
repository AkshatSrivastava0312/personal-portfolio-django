from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactForm
import requests
import json
from datetime import date,datetime
import pytz
from about.models import SocialLink

# Create your views here.
def show(request):
    if request.method == 'POST':
        social_obj = SocialLink.objects.all()[0]
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        clientKey = request.POST.get('g-recaptcha-response')
        secretKey = '6Le-LdoaAAAAAD_8DdKg-T9cFjXcNtWjR-4yBInG'
        captchaData = {'secret':secretKey,'response':clientKey}
        request_google = requests.post('https://www.google.com/recaptcha/api/siteverify',data=captchaData)
        response_google = json.loads(request_google.text)
        verifyCaptcha = response_google['success']
        if verifyCaptcha:
            currentDate = date.today()
            localTime = pytz.timezone('Asia/Kolkata')
            currentTime = datetime.now(localTime).time()
            contact_entry = ContactForm(name=name,email=email,subject=subject,message=message,postDate=currentDate,postTime=currentTime)
            contact_entry.save()
            return render(request,'contact.html',{'post':'yes','social_data':social_obj})        
        else:
            return render(request,'contact.html',{'notPost':'yes','social_data':social_obj})
    social_obj = SocialLink.objects.all()[0]
    return render(request,'contact.html',{'social_data':social_obj})
    