# Generated by Django 2.0.4 on 2018-07-14 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boyScouts', '0007_badge_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='group_user',
            name='section',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='boyScouts.Section'),
            preserve_default=False,
        ),
    ]
