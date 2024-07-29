from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class User(AbstractUser):
    g = [
        ('0','--- Select Your Gender ---'),
        ('1','Male'),
        ('2','Female'),
        ('3','Other')
    ]
    c = [
        ('0','--- Select Your Role Type ---'),
        ('1','Team Lead'),
        ('2','Agent'),
    ]
    Mobile_Number = models.CharField(max_length=10,null=True,blank=True)
    Gender = models.CharField(choices=g,default='0',max_length=5)
    Role_Type = models.CharField(choices=c,default='0',max_length=5)
    Profile_Image = models.ImageField(upload_to='Profiles/',default='Profiles/profile.png')
    City_or_Village = models.CharField(max_length=50,null=True,blank=True)
    Mandal = models.CharField(max_length=50,null=True,blank=True)
    District = models.CharField(max_length=50,null=True,blank=True)
    State = models.CharField(max_length=50,null=True,blank=True)

class Project(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    team_lead=models.CharField(max_length=200,null=True,blank=True)
    category=models.CharField(max_length=200,null=True,blank=True)
    points = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.title

class ProjectRequest(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    started = models.BooleanField(default=False)
    requested_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('project', 'agent')

class ProjectStatus(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    started = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.project.title} - Status'
