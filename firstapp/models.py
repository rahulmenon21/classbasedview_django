from django.db import models
from django import forms

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField(max_length=30)

    class Meta:
        db_table = 'employee'


class Empform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'