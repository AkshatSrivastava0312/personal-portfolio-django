from django.db import models

# Create your models here.
class AboutImage(models.Model):
    class Meta:
        verbose_name_plural = "About Image"
    imageName = models.TextField(max_length=100)
    imageUrl = models.ImageField(upload_to="about/image")
    postDate = models.DateField()

    def __str__(self):
        return self.imageName + " Posted On : " + str(self.postDate)

class AboutText(models.Model):
    class Meta:
        verbose_name_plural = "About Text"

    aboutText = models.TextField()
    postDate = models.DateField()

    def __str__(self):
        return self.aboutText[:100] + ".... Posted On : " + str(self.postDate)


class CV(models.Model):
    class Meta:
        verbose_name_plural = "CV"

    cvTitle = models.TextField(max_length = 100)
    attachement = models.FileField(upload_to="about/cv")
    postDate = models.DateField()

    def __str__(self):
        return self.cvTitle + " Posted On : " + str(self.postDate)

class SocialLink(models.Model):
    class Meta:
        verbose_name_plural = "Social Links"

    githubLink = models.URLField()
    linkedinLink = models.URLField()
    postDate = models.DateField()

    def __str__(self):
        return "Posted links for github : " + str(self.githubLink) + " and " + " linkedin: " + str(self.linkedinLink) + " on " + str(self.postDate)
    
    