# Generated by Django 2.2.14 on 2020-08-12 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200805_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='access',
            name='recent',
            field=models.DateTimeField(auto_now=True),
        ),
    ]