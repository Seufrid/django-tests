# Generated by Django 4.2.7 on 2023-12-28 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heartify', '0011_alter_selftestresult_result'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='selftestresult',
            options={'verbose_name': 'SelfTest Result', 'verbose_name_plural': 'SelfTest Results'},
        ),
    ]
