# Generated by Django 3.2 on 2022-03-12 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('contact', models.IntegerField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
