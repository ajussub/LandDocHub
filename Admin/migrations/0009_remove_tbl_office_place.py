# Generated by Django 4.2.8 on 2024-03-11 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0008_alter_tbl_services_services_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_office',
            name='place',
        ),
    ]