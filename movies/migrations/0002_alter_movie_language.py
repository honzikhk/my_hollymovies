# Generated by Django 4.0.3 on 2022-03-27 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(choices=[('eng', 'english'), ('cz', 'czech')], max_length=5),
        ),
    ]