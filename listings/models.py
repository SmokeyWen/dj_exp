from django.db import models
from datetime import datetime
from authors.models import Author

# Create your models here.
class Listing(models.Model):
    author = models.ForeignKey(Author, on_delete = models.DO_NOTHING)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    duration = models.IntegerField()
    height = models.FloatField()
    width = models.FloatField()
    initial_price = models.FloatField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    complete_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title