from django.db import models

class Hotels(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=250, null=False)
    price = models.IntegerField()

    def __str__(self):
        return self.name
