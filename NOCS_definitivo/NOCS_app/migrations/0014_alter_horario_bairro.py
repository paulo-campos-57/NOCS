# Generated by Django 4.1.7 on 2023-05-07 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NOCS_app', '0013_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='bairro',
            field=models.TextField(default='-'),
        ),
    ]
