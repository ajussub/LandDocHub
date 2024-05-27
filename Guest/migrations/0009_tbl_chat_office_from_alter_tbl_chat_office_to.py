# Generated by Django 4.2.8 on 2024-03-15 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0008_alter_tbl_chat_office_to_alter_tbl_chat_user_from_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_chat',
            name='office_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='office_from', to='Guest.tbl_office'),
        ),
        migrations.AlterField(
            model_name='tbl_chat',
            name='office_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='office_to', to='Guest.tbl_office'),
        ),
    ]