# Generated by Django 4.2.20 on 2025-03-16 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cc', models.CharField(max_length=20, unique=True)),
                ('edad', models.IntegerField()),
                ('genero', models.CharField(max_length=10)),
            ],
        ),
    ]
