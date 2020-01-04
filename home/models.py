from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.pk + ' - ' + self.name


# class Product(models.Model):
#     category = models.OneToOneRel(Category, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='media/img/product')
#     size = models.CharField(max_length=10)
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#     quantity = models.IntegerField()
#     rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True)
#     is_active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.pk + ' - ' + self.name
#
#
# class Rating(models.Model):
#     rating = models.DecimalField(blank=True)
#     product = models.ManyToOneRel(to=Product, field_name='name')
#     review = models.TextField(blank=True)
