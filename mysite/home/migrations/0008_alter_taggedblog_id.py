# Generated by Django 3.2.8 on 2021-10-06 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_blogtag_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taggedblog',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
