from django.db import models

# Create your models here.

class Pet(models.Model):

    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    # List of sex choices,
    # where the 1st value is what's stored in the DB
    # and the 2nd is used to display in forms and the admin

    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    sex = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    # set null to True instead of blank True for integerField.
    # blank integer results in zero
    vaccinations = models.ManyToManyField('Vaccine', blank='True')



class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
