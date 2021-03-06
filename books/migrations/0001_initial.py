# Generated by Django 4.0.3 on 2022-04-10 11:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=100)),
                ('born_at', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('language', models.CharField(choices=[('eng', 'english'), ('cz', 'czech')], max_length=5)),
                ('genres', models.CharField(choices=[('drama', 'drama'), ('comedy', 'comedy'), ('thriller', 'thriller'), ('romance', 'romance')], max_length=10)),
                ('released', models.DateField()),
                ('likes', models.IntegerField(default=0)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='books.author')),
            ],
        ),
    ]
