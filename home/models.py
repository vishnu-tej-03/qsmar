from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.


class User(AbstractUser):
    is_hod = models.BooleanField(default=False)
    location = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=254)
    company = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)


class Qsmart(models.Model):
    Samplename = models.CharField(max_length=500, blank=True, null=True)
    Sampledesc = models.CharField(max_length=500, blank=True, null=True)
    UserName = models.CharField(max_length=30, blank=True)
    Qremarks = models.CharField(max_length=500, blank=True, null=True)
    Value_F1 = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    Value_F2 = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    Value_F3 = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    Value_F4 = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    Value_F5 = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    Value_F6 = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    Value_F7 = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    Value_F8 = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    Value_F9 = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    Value_F10 = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    QSMAR_rating = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)


class Remarks(models.Model):
    Range_min = models.IntegerField()
    Range_high = models.IntegerField()
    category = models.CharField(max_length=100, blank=True, null=True)
    StabilityslopeRemark = models.CharField(
        max_length=100, blank=True, null=True)
    Failures = models.CharField(max_length=100, blank=True, null=True)
    Remborder = models.CharField(max_length=100, blank=True, null=True)


class Suggestion(models.Model):
    min = models.IntegerField()
    high = models.IntegerField()
    Support_suggested = models.CharField(max_length=200, blank=True, null=True)
