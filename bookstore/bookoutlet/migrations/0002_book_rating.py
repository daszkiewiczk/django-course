# Generated by Django 4.2.5 on 2023-09-14 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookoutlet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
