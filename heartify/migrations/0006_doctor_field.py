# Generated by Django 4.2.7 on 2023-12-17 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heartify', '0005_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='field',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
