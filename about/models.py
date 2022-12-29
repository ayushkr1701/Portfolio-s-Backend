from django.db import models


class About(models.Model):
  title = models.CharField(max_length=50)
  SchoolName = models.CharField(max_length=250)
  CGPA = models.CharField(max_length=250)
  icon = models.CharField(max_length=30) # Material Icon name
  
  class Meta:
    verbose_name = 'Education'
    verbose_name_plural = 'Education'
    
  def __str__(self):
    return self.title