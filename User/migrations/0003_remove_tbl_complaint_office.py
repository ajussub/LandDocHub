# Generated by Django 4.2.8 on 2024-03-11 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_alter_tbl_complaint_office'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_complaint',
            name='office',
        ),
    ]
