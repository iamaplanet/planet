# Generated by Django 3.0.8 on 2020-08-15 07:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_remove_costumer_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='costumer',
            name='application_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
