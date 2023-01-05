from django.db import models
from  django.utils import timezone
import datetime
# Create your models here.
class Benh(models.Model):
    ten_benh = models.CharField(max_length=200)
    kh = models.CharField(max_length=50)
    nguyen_nhan = models.TextField(blank=True)
    dieu_tri = models.TextField(blank=True)

    def __str__(self):
        return self.ten_benh

class TrieuChung(models.Model):
    ten = models.CharField(max_length=200)
    ki_hieu = models.CharField(max_length=50)

    def __str__(self):
        return self.ten

class GiaTri(models.Model):
    benh = models.ForeignKey(Benh, on_delete=models.CASCADE)
    tc = models.ForeignKey(TrieuChung, on_delete=models.CASCADE)
    gia_tri = models.FloatField(default=0)
    trongso = models.IntegerField(default=1)


    def __str__(self):
        return self.benh.ten_benh + "--"+self.tc.ten

class User(models.Model):
    ten = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    matkhau = models.CharField(max_length=45)

    def __str__(self):
        return self.ten

class BenhAn(models.Model):
    tenbenh = models.CharField(max_length=200)
    ngaychuandoan = models.DateTimeField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)