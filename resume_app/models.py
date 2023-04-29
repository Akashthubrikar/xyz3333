from django.db import models

# Create your models here.
from django.db import models
from multiselectfield import MultiSelectField

class Candidate(models.Model):
    class TechChoices (models.TextChoices):
        Python= 'Python'
        Java='Java'
        Ruby= 'Ruby'
        Docker='Docker'
        Node= 'Node'
        JS='JS'
    
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(max_length=255)
    tech_skills = MultiSelectField(choices=TechChoices.choices, max_length=255)
    experience=models.TextField()