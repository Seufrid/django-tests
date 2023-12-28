# Generated by Django 4.2.7 on 2023-12-28 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heartify', '0009_selftestresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='selftestresult',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='selftestresult',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]