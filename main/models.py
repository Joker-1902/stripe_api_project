from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    description = models.TextField(max_length=255, blank=True, null=True)
    price = models.DecimalField(default=0.00,max_digits=7,decimal_places=2)

    def __str__(self):
        return self.name