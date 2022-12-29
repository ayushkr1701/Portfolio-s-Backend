from django.contrib import admin
from .models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
  list_display = ('id', 'Tenure', 'Company', 'Designation')
  list_display_links = ('id', 'Company')
  search_fields = ('Tenure', 'Company', 'Designation')
  list_per_page = 20

admin.site.register(Testimonial, TestimonialAdmin)
