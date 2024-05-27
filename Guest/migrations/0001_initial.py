# Generated by Django 4.2.8 on 2024-03-11 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0004_tbl_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_contact', models.IntegerField(null=True)),
                ('user_email', models.EmailField(max_length=50)),
                ('user_gender', models.CharField(max_length=50)),
                ('user_address', models.CharField(max_length=50)),
                ('user_photo', models.FileField(upload_to='userdocs/')),
                ('user_proof', models.FileField(upload_to='userdocs/')),
                ('user_password', models.CharField(max_length=50)),
                ('user_status', models.IntegerField(default=0)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
    ]