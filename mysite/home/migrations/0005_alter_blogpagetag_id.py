# Generated by Django 3.2.8 on 2021-10-06 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20211006_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpagetag',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
