# Generated by Django 5.1.1 on 2024-10-16 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='contname',
            new_name='contactname',
        ),
    ]