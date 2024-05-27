# Generated by Django 4.2.8 on 2024-03-15 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0009_tbl_chat_office_from_alter_tbl_chat_office_to'),
        ('User', '0006_tbl_servicerequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_data', models.IntegerField()),
                ('user_name', models.CharField(max_length=500)),
                ('user_review', models.CharField(max_length=500)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_office')),
            ],
        ),
    ]
