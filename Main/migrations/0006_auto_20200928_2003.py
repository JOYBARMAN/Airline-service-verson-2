# Generated by Django 3.1.1 on 2020-09-28 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_auto_20200926_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sflight', models.CharField(max_length=122)),
                ('passport_num', models.CharField(max_length=122)),
            ],
        ),
        migrations.RemoveField(
            model_name='flight',
            name='sflight',
        ),
    ]
