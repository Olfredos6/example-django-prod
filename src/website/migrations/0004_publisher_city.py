# Generated by Django 4.2 on 2023-12-06 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='city',
            field=models.CharField(default='Paris', max_length=50),
            preserve_default=False,
        ),
    ]