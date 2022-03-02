from django.db import models

# Create your models here.
class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    price = models.IntegerField()
    city = models.CharField(max_length=400, null=False)
    starRating = models.IntegerField()
    amenities = models. CharField(max_length=500, null=True)
    noDaysBooked = models.IntegerField(default=0)
    finalCost = models.IntegerField(default=0)

    def __str__(self):
        return (str(self.id) + ': '+ self.name)