# Generated by Django 4.1.7 on 2023-04-09 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensagens',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('email', models.TextField(max_length=355)),
                ('texto', models.TextField(max_length=1000)),
            ],
        ),
    ]