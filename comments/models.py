from django.db import models
from datetime import datetime
from listings.models import Listing

# Create your models here.
class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete = models.DO_NOTHING)
    title = models.CharField(max_length=250)
    message = models.TextField(max_length=500)
    date = models.DateTimeField(default = datetime.now, blank = True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.title