from django.db import models


class Testimonial(models.Model):
  Tenure = models.CharField(max_length=100)
  Company = models.CharField(max_length=100)
  Designation = models.CharField(max_length=100)
  # testimonial = models.CharField(max_length=300)
  # author_name = models.CharField(max_length=100)
  # author_title = models.CharField(max_length=100)
  # author_photo = models.ImageField(upload_to='images')
  
  class Meta:
    verbose_name = 'Experience'
    verbose_name_plural = 'Experiences'
    
  def __str__(self):
    return self.Company