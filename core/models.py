from django.db import models

# Create your models here.

# About Model
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    about_link = models.URLField(max_length=100)
    image = models.ImageField(upload_to='about')

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"

# Service Model
class Service(models.Model):
    name = models.CharField(max_length=150, verbose_name="Service name")
    description = models.TextField(verbose_name="About Service")

    def __str__(self):
        return self.name


# Recent work model
class RecentWork(models.Model):
    title = models.CharField(max_length=100, verbose_name="Work title")
    image = models.ImageField(upload_to="works")

    def __str__(self):
        return self.title

# Client model
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Client name")
    description = models.TextField(verbose_name="Client say")
    image = models.ImageField(upload_to="clients", default="default.png")

    def __str__(self):
        return self.name
