from django.db import models

class product(models.Model):
    Product_Name = models.CharField(max_length=120)
    Product_Type = models.CharField(max_length=120)
    Product_Price = models.DecimalField(max_digits=20000,decimal_places=3)
    Product_Description = models.TextField(blank=True)
    Product_Quantity = models.IntegerField()

    def __str__(self):
        return self.Product_Name
