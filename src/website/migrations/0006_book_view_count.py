# Generated by Django 4.2 on 2023-12-06 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_remove_publisher_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
