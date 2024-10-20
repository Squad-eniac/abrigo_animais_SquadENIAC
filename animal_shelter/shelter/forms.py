from django import forms
from .models import Animal, Adoption, Staff

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'species', 'age', 'breed', 'healthy_history']

class AdoptionForm(forms.ModelForm):
    class Meta:
        model = Adoption
        fields = ['animal_name', 'species', 'adopter', 'request_date', 'status']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'phone', 'role']