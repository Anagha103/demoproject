# Generated by Django 5.1.1 on 2024-10-16 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contname', models.CharField(max_length=50, unique=True)),
                ('contnumb', models.IntegerField(default=1)),
            ],
        ),
    ]
