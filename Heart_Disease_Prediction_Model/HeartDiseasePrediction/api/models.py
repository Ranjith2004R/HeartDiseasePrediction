from django.db import models

class MedicalData(models.Model):
    age = models.FloatField()
    gender = models.IntegerField()
    heart_rate = models.FloatField()
    systolic_bp = models.FloatField()
    diastolic_bp = models.FloatField()
    blood_sugar = models.FloatField()
    ck_mb = models.FloatField()
    troponin = models.FloatField()
