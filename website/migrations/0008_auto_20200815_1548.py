# Generated by Django 3.0.8 on 2020-08-15 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20200815_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Costumer'),
        ),
    ]
