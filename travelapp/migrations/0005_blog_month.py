# Generated by Django 3.2.4 on 2021-07-04 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0004_blog_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='month',
            field=models.CharField(default=5, max_length=100),
            preserve_default=False,
        ),
    ]