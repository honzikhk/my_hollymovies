# Generated by Django 4.0.3 on 2022-04-15 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='on_shelf',
            field=models.BooleanField(default=False),
        ),
    ]
