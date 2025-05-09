# Generated by Django 5.1 on 2024-12-17 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rotaryapp', '0006_sponsor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uyare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('phone_number', models.CharField(max_length=15)),
                ('qualification', models.CharField(max_length=50)),
            ],
        ),
    ]
