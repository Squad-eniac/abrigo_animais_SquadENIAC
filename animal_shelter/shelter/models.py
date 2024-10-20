from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=30)
    species = models.CharField(max_length=30)
    age = models.IntegerField()
    breed = models.CharField(max_length=30)
    health_history = models.TextField()

    def __str__(self):
        return f'{self.name}: {self.species} - {self.age} - {self.breed} - {self.health_history}'
    
    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animals'
        ordering = ['name']

class Adoption(models.Model):
    status =(
        ('Not Adopted', 'Not Adopted'),
        ('Adopted', 'Adopted')
    )
    animal_name = models.CharField(max_length=30)
    species = models.CharField(max_length=30)
    adopter = models.CharField(max_length=30)
    request_date = models.DateField(help_text='aaaa/mm/dd')
    status = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.animal_name}: {self.species} - {self.adopter} - {self.request_date} - {self.status}'
    
    class Meta:
        verbose_name = 'Adoption'
        verbose_name_plural = 'Adoptions'
        ordering = ['request_date']


class Staff(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    role = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}: {self.phone} - {self.role}'
    
    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'
        ordering = ['name']
