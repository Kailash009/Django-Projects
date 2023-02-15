from django.db import models

# Create your models here.
dept=[
    ('General Health','General Health'),
    ('Cardiology','Cardiology'),
    ('Dental','Dental'),
    ('Medical Research','Medical Research'),
]

class Appointment(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    date=models.DateField()
    department=models.CharField(max_length=200,choices=dept)
    mobile=models.CharField(max_length=18)
    message=models.TextField()
    def __str__(self):
        return self.name
    


    
