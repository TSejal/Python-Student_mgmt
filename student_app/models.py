from django.db import models
from django.utils import timezone


# Create your models here.

class School(models.Model):
    school_reting = (
			('one', '1'),
			('two', '2'), 
			('three', '3'),
            ('four', '4'),
        	('five', '5'),
		)

    name = models.CharField(max_length=50)
    address = models.TextField(blank=True,null=True)
    rating = models.CharField(choices=school_reting,max_length=50)
    email = models.EmailField()
    contact_no = models.CharField(max_length=10,null=True,blank=True)
    websit = models.CharField(max_length=50,null=True,blank=True)
    enabled = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField()

    def __str__(self):
        return self.name

class Student(models.Model):
    student_stsndard = (
        ('five','5'),
        ('six','6'),
        ('seven','7'),
        ('eight','8'),
        ('nine','9'),
        ('ten','10'),
    )
    school = models.ForeignKey(School)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    residence_address = models.TextField(null=True,blank=True)
    standard = models.CharField(choices=student_stsndard,max_length=50)
    roll_no = models.IntegerField()
    fees = models.IntegerField()
    enabled = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField()
    def __str__(self):
        return self.first_name
