from django.db import models


class Catalog(models.Model):
    name = models.CharField(choices=[('сварка', 'сварка'), ('котлы', 'котлы'),
                                     ('плазменная резка', 'плазменная резка'),
                                     ('ворота', 'ворота'), ('калитки', 'калитки'),
                                     ('другое', 'другое'), ('все', 'все')], max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):    
    title = models.CharField(max_length=100)
    catalog = models.ForeignKey(Catalog, null=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    price = models.IntegerField()
    img = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title
