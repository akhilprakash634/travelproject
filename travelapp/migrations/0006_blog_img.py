# Generated by Django 3.2.4 on 2021-07-05 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0005_blog_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='img',
            field=models.ImageField(default=5, upload_to='picture'),
            preserve_default=False,
        ),
    ]
