# Generated by Django 4.1.7 on 2023-04-20 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NOCS_app', '0006_rename_password_cadastro_password1'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='bairro',
            field=models.TextField(default='-'),
        ),
    ]
