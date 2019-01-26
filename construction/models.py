# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Contact(models.Model):
	Name = models.CharField(max_length=100)
	Phone_Number = models.CharField(max_length=10,blank=True)
	Email = models.EmailField()
	Subject = models.CharField(max_length=100)
	Message = models.TextField(max_length=500)
	
	def __str__(self):
		return self.Email
class Worker(models.Model):
	PROFESSION_CHOICES = (
    	('Welder', 'Freshman'),
    	('Helper', 'Helper'),
    	('Sweeper', 'Sweeper'),
    	('Maid', 'Maid'),
	)
	Name = models.CharField(max_length=100)
	Phone_Number = models.CharField(max_length=10)
	Email = models.EmailField(blank=True)
	Address = models.TextField(max_length=500)
	Profession = models.CharField(max_length=50,choices=PROFESSION_CHOICES)

	def __str__(self):
		return str(self.id)+' '+self.Name +' '+self.Profession+' '+self.Phone_Number

class Nation(models.Model):
	Name = models.CharField(max_length=100)
	alpha2_code = models.CharField(max_length=10,blank=True)
	alpha3_code = models.CharField(max_length=10,blank=True)

	def __str__(self):
		return self.Name
