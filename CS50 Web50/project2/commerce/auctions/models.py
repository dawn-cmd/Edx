from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    watchlist = models.ManyToManyField('Auction_listing', related_name='watch_user', blank=True)

class Categories(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Auction_listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=10000)
    cover_url = models.CharField(max_length=2000)
    provider = models.ForeignKey(User, on_delete=models.PROTECT, related_name="items", default=None)
    category = models.ForeignKey(Categories, on_delete=models.PROTECT,related_name="items", default=None)
    bidder = models.ForeignKey(User, on_delete=models.PROTECT, related_name="bid_items", default=None)
    bid = models.IntegerField(default=0)
    active = models.BooleanField(default=True) 

class Comment(models.Model):
    content = models.CharField(max_length=999999)
    commenter = models.ForeignKey(User, on_delete=models.PROTECT, related_name="comment", default=None)
    item = models.ForeignKey(Auction_listing, on_delete=models.PROTECT, related_name="comment", default=None)
    
    def __str__(self) -> str:
        return self.content
