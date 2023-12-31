# Generated by Django 4.2.7 on 2023-12-28 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heartify', '0016_appointment_email_appointment_name_contact_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personprofile',
            options={'verbose_name': 'User Profiles', 'verbose_name_plural': 'User Profiles'},
        ),
        migrations.AlterModelOptions(
            name='selftestresult',
            options={'verbose_name': 'SelfTest Result', 'verbose_name_plural': 'SelfTest Results'},
        ),
        migrations.AlterField(
            model_name='personprofile',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
