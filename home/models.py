from django.db import models

# Create your models here.
class Tagline(models.Model):
    class Meta:
        verbose_name_plural = "Tagline"

    title = models.TextField(max_length=25)
    text = models.TextField(max_length=250)
    postDate = models.DateField()

    def __str__(self):
        return self.title + " posted on " + str(self.postDate)
        

class TopSkills(models.Model):
    class Meta:
        verbose_name_plural = "Top Skills"

    skillName1Title = models.TextField(max_length=20)
    skillName1Description = models.TextField(max_length=200)
    skillName2Title = models.TextField(max_length=20)
    skillName2Description = models.TextField(max_length=200) 
    skillName3Title = models.TextField(max_length=20)
    skillName3Description = models.TextField(max_length=200)
    postDate = models.DateField()

    def __str__(self):
        return self.skillName1Title + ", " + self.skillName2Title + ", " + self.skillName3Title + " Posted on " + str(self.postDate)

class ImageGallery(models.Model):
    class Meta:
        verbose_name_plural = "Image Gallery"

    imageUrl = models.ImageField(upload_to='home/gallery',default="")
    imageTitle = models.TextField(max_length=50)
    imageSubtitle = models.TextField(max_length=100)
    imageText = models.TextField(max_length=500)
    postDate = models.DateField()

    def __str__(self):
        return self.imageTitle + ", Posted On: " + str(self.postDate)

