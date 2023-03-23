from django.contrib import admin
from .models import User, Categories, Auction_listing, Comment
# Register your models here.
admin.site.register(User)
admin.site.register(Categories)
admin.site.register(Auction_listing)
admin.site.register(Comment)