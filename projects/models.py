from django.db import models

# Create your models here.
class Project(models.Model):
    projectTitle = models.TextField(max_length = 200) 
    projectDescription = models.TextField(max_length = 500)
    projectUrl = models.URLField(max_length=1000)
    postDate = models.DateField()

    def __str__(self):
        return self.projectTitle + " Posted On : " + str(self.postDate)
    