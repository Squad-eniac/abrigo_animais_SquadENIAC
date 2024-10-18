from django.contrib import admin
from .models import Animal, Adoption, Staff


class AnimalAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'age', 'breed', 'health_history']
    search_fields = ['name', 'species', 'breed']
    list_filter = ['species', 'breed']
    ordering = ['species']


class AdoptionAdmin(admin.ModelAdmin):
    list_display = ['animal_name', 'species', 'adopter', 'request_date', 'status']
    search_fields = ['animal_name', 'species', 'adopter', 'request_date', 'status']
    list_filter = ['species', 'request_date', 'status']
    ordering = ['request_date']


class StaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'role']
    search_fields = ['name', 'role']
    list_filter = ['role']
    ordering = ['name']


admin.site.register(Animal)
admin.site.register(Adoption)
admin.site.register(Staff)
