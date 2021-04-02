from django.db import models

# Create your models here.
class Stock(models.Model):
    ticker = models.CharField(max_length=10)
    primaryExchange=models.CharField(max_length=50, default="NSE")
    week52Low=models.IntegerField(default=1)
    week52High=models.IntegerField(default=1)

    def __str__(self):
        return self.ticker
    