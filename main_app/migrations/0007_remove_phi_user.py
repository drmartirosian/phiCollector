# Generated by Django 3.0 on 2020-01-02 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_phi_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phi',
            name='user',
        ),
    ]
