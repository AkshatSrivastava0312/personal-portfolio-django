from django.contrib import admin
from .models import Tagline,TopSkills,ImageGallery
from django.contrib.auth.models import User, Group

class TaglineAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # check if generally has add permission
        retVal = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if retVal and Tagline.objects.exists():
            retVal = False
        return retVal

class TopSkillsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # check if generally has add permission
        retVal = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if retVal and TopSkills.objects.exists():
            retVal = False
        return retVal

# Register your models here.
admin.site.register(Tagline,TaglineAdmin)
admin.site.register(TopSkills,TopSkillsAdmin)
admin.site.register(ImageGallery)


# Unregistering User Tables
admin.site.unregister(Group)
admin.site.unregister(User)