# Generated by Django 4.2.8 on 2024-03-11 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_admin',
        ),
        migrations.DeleteModel(
            name='tbl_brand',
        ),
        migrations.RemoveField(
            model_name='tbl_office',
            name='place',
        ),
        migrations.RemoveField(
            model_name='tbl_place',
            name='district',
        ),
        migrations.DeleteModel(
            name='tbl_product',
        ),
        migrations.DeleteModel(
            name='tbl_services',
        ),
        migrations.RemoveField(
            model_name='tbl_subcategory',
            name='category',
        ),
        migrations.DeleteModel(
            name='tbl_type',
        ),
        migrations.DeleteModel(
            name='tbl_category',
        ),
        migrations.DeleteModel(
            name='tbl_district',
        ),
        migrations.DeleteModel(
            name='tbl_office',
        ),
        migrations.DeleteModel(
            name='tbl_place',
        ),
        migrations.DeleteModel(
            name='tbl_subcategory',
        ),
    ]