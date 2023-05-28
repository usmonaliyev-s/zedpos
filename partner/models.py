from django.db import models

# Create your models here.
class Dealer(models.Model):
    name = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class DealerOutput(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.SET_NULL, null=True)
    price = models.IntegerField()
    date = models.DateField(auto_now=True)
    worker = models.ForeignKey("accounts.CustomUser", on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
