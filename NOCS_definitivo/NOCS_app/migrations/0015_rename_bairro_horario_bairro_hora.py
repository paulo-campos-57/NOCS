# Generated by Django 4.1.7 on 2023-05-07 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NOCS_app', '0014_alter_horario_bairro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='horario',
            old_name='bairro',
            new_name='bairro_hora',
        ),
    ]