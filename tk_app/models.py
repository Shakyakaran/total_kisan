from django.db import models

class AddCrop(models.Model):


    userEmail = models.CharField(max_length=70)
    state = models.CharField(max_length=50,default='')
    dist = models.CharField(max_length=50,default='')
    block = models.CharField(max_length=50,default='')
    vill = models.CharField(max_length=50,default='')
    cropName = models.CharField(max_length=50)
    cropVariety = models.CharField(max_length=50,default='')
    cropArea = models.IntegerField()
    startDate = models.DateField(auto_now=False, auto_now_add=False)
    endDate = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return (self.userEmail)

