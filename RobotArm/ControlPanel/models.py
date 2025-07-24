from django.db import models

class Pose(models.Model):
    motor1 = models.IntegerField()
    motor2 = models.IntegerField()
    motor3 = models.IntegerField()
    motor4 = models.IntegerField()
    motor5 = models.IntegerField()
    motor6 = models.IntegerField()

    def __str__(self):
        return f"Pose {self.id}"

class Run(models.Model):
    motor1 = models.IntegerField()
    motor2 = models.IntegerField()
    motor3 = models.IntegerField()
    motor4 = models.IntegerField()
    motor5 = models.IntegerField()
    motor6 = models.IntegerField()
    status = models.IntegerField(default=0)

    def __str__(self):
        return f"Run: S1={self.servo1}, ..., Status={self.status}"