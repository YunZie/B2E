# Generated by Django 2.2.5 on 2020-01-10 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200111_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store_tinyurl',
            name='short_key',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
