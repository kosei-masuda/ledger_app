from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BookModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    memo = models.TextField(null=True, blank=True, default='')
    income = models.IntegerField()
    expenses = models.IntegerField()
    date = models.DateField()
    kind = models.CharField(max_length=10)

class PreviousMonthData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income = models.IntegerField(null=True, blank=True, default=0)
    expenses = models.IntegerField(null=True, blank=True, default=0)
    total = models.IntegerField(null=True, blank=True, default=0)









