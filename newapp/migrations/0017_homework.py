# Generated by Django 4.1.4 on 2023-01-29 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0016_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cm', models.CharField(max_length=150)),
                ('homeworks', models.FileField(upload_to='homeworks/')),
            ],
        ),
    ]
