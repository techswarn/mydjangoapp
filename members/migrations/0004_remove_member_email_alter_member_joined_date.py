# Generated by Django 4.1.4 on 2023-12-08 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_member_email_member_updated_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='email',
        ),
        migrations.AlterField(
            model_name='member',
            name='joined_date',
            field=models.DateField(null=True),
        ),
    ]
