# Generated by Django 4.1.5 on 2023-01-05 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountbookrecords', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountbookrecord',
            name='serial_no',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
