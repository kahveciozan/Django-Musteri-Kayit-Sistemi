# Generated by Django 3.1.3 on 2020-11-19 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('tc', models.CharField(max_length=11)),
                ('gsm', models.CharField(max_length=10)),
            ],
        ),
    ]
