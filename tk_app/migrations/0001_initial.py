# Generated by Django 4.1.7 on 2023-03-16 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddCrop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userEmail', models.CharField(max_length=70)),
                ('state', models.CharField(default='', max_length=50)),
                ('dist', models.CharField(default='', max_length=50)),
                ('block', models.CharField(default='', max_length=50)),
                ('vill', models.CharField(default='', max_length=50)),
                ('cropName', models.CharField(max_length=50)),
                ('cropVariety', models.CharField(max_length=50)),
                ('cropArea', models.IntegerField()),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
            ],
        ),
    ]