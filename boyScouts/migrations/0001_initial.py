# Generated by Django 2.0.4 on 2018-07-07 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fatherName', models.CharField(max_length=50)),
                ('dateOFBirth', models.DateField()),
                ('contactNumber', models.CharField(max_length=11)),
                ('cnic', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
                ('secularEducation', models.CharField(max_length=20)),
                ('religiousEducation', models.CharField(max_length=14)),
                ('bloodGroup', models.CharField(max_length=30)),
                ('residentialAddress', models.CharField(max_length=256)),
                ('transferForm', models.CharField(max_length=256)),
            ],
        ),
    ]
