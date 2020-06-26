from django.db import models

class User(models.Model):
    Real_Name = models.CharField('Name',max_length=100)
    Timezone = models.CharField('Timezone',max_length=100)

class Activity(models.Model):
    User_Id = models.ForeignKey(User, on_delete= models.CASCADE)
    Start_Time = models.CharField('StartTime', max_length=100)
    End_Time = models.CharField('EndTime', max_length=100)