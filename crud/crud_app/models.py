

from django.db import models

class Car_classification(models.Model):
    classification = models.CharField(max_length=20)
    def __str__(self):
        return self.classification

class Car(models.Model):
    car_brand = models.CharField(max_length=20)
    car_model = models.CharField(max_length=20)
    car_color = models.CharField(max_length=10)
    car_classification = models.ForeignKey(Car_classification, on_delete=models.CASCADE)

    def __str__(self):
        return self.car_brand

