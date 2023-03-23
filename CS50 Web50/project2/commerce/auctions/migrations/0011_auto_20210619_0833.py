# Generated by Django 3.2.4 on 2021-06-19 00:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auto_20210619_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_listing',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='items', to='auctions.categories'),
        ),
        migrations.AlterField(
            model_name='auction_listing',
            name='provider',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='items', to=settings.AUTH_USER_MODEL),
        ),
    ]
