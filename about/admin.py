from django.contrib import admin
from .models import AboutImage,AboutText,CV,SocialLink

class AboutImageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # check if generally has add permission
        retVal = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if retVal and AboutImage.objects.exists():
            retVal = False
        return retVal

class AboutTextAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # check if generally has add permission
        retVal = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if retVal and AboutText.objects.exists():
            retVal = False
        return retVal
        
class SocialLinkAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # check if generally has add permission
        retVal = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if retVal and SocialLink.objects.exists():
            retVal = False
        return retVal


class CVAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # check if generally has add permission
        retVal = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if retVal and CV.objects.exists():
            retVal = False
        return retVal
        
# Register your models here.
admin.site.register(AboutImage,AboutTextAdmin)
admin.site.register(AboutText,AboutTextAdmin)
admin.site.register(CV,CVAdmin)
admin.site.register(SocialLink,SocialLinkAdmin)
