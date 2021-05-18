from django.db import models

# Create your models here.
class ContactForm(models.Model):
    name = models.TextField()
    email = models.TextField()
    subject = models.TextField()
    message = models.TextField()
    postDate = models.DateField()
    postTime = models.TimeField()

    def __str__(self):
        return self.subject + " Posted By: " + self.name + " On " + str(self.postDate) + " At " + str(self.postTime)
    