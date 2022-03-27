from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserMine(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default='profile1.png',null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name


class Movie(models.Model):
    LANGUAGE_CHOICES = (
        ('EN', 'ENGLISH'),
        ('GR', 'GERMAN'),
        ('RU', 'RUSSIAN')

    )
    STATUS_CHOICES = (
        ("Eng ko'p ko'rilgan", "Eng ko'p ko'rilgan"),
        ("Eng ko'p yuklangan", "Eng ko'p yuklangan"),
        ("Eng reytingi baland", "Eng reytingi baland"),
    )

    title = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=200, null=True)
    image = models.ImageField( null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50)
    year_of_production = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    views_count = models.IntegerField(default=0)
    category = models.ManyToManyField(Tag)
    video = models.FileField(upload_to='video/',null=True)

    def __str__(self):
        return self.title




class Order(models.Model):
    STATUS_CHOICES = (
        ("Ko'rilmagan", "Ko'rilmagan"),

        ("Ko'rib bo'lingan", "Ko'rib bo'lingan"),
    )
    customer = models.ForeignKey(UserMine, null=True, on_delete=models.SET_NULL)
    movie = models.ForeignKey(Movie, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50)