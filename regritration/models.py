from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

classes=(
        ("PRY_1" , "Primary 1"),
        ("PRY_2" , "Primary 2"),
        ("PRY_3" , "Primary 3"),
        ("PRY_4" , "Primary 4"),
        ("PRY_5" , "Primary 5"),
        ("PRY_6" , "Primary 6"),
    )


user = get_user_model()

class Reg(models.Model):
    
    author = models.ForeignKey(user, on_delete=models.CASCADE)

    Sur_name = models.CharField(max_length=20, blank=False, null=True)
    First_name = models.CharField(max_length=20, blank=False, null=True)
    Middle_name = models.CharField(max_length=20, blank=False, null=True)
    Date_of_birth = models.DateField(("Date"), default=datetime.now())
    Age = models.PositiveIntegerField(null=True, blank=False)
    Photo = models.ImageField(upload_to="photo/", blank=True, null=True)
    Postal_Address = models.TextField(max_length=1100, blank=False, null=True)
    Residential_Address = models.TextField(max_length=1100, blank=False, null=True)
    #models.TextField(max_length=2000, blank=False, null=True)
    Latest_School_Address = models.TextField(max_length=2000, blank=False, null=True)
    Latest_class_Attended = models.CharField(max_length=30, choices=classes, default="PRY_1")
    Home_Telephone_Number = models.CharField(max_length=11, blank=False, null=True)
    Name_of_Father = models.CharField(max_length=200, blank=False, null=True)
    Occpation_of_Father = models.CharField(max_length=200, blank=False, null=True)
    Contact_Address_of_Father = models.TextField(max_length=1100, blank=False, null=True)
    Tel_No_of_Father = models.CharField(max_length=11, blank=False, null=True)
    Name_of_Mother = models.CharField(max_length=200, blank=False, null=True)
    Occpation_of_Mother = models.CharField(max_length=200, blank=False, null=True)
    Contact_Address_of_Mother = models.TextField(max_length=1100, blank=False, null=True)
    Tel_No_of_Mother = models.CharField(max_length=11, blank=False, null=True)
    In_case_of_any_emergency_contact = models.TextField(max_length=1100, blank=False, null=True)
    Any_allery_or_physical_defect = models.TextField(max_length=1100, blank=False, null=True)


    #def __str__(self):
    #    return self.First_name

    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])
        #return reverse("detail")
