# Generated by Django 3.2.4 on 2021-07-04 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0003_auto_20210704_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(default=4, max_length=100),
            preserve_default=False,
        ),
    ]