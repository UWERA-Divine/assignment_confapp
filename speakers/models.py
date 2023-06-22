from django.db import models

class Speakers(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    gender = models.CharField(max_length = 255)

    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender

def __str__(self):
    return f"{first_name} {last_name}"    
