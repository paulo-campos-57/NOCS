# Generated by Django 4.1.7 on 2023-04-20 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NOCS_app', '0008_cadastro_rua'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='numero',
            field=models.IntegerField(default=0),
        ),
    ]
