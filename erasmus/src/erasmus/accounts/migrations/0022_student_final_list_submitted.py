# Generated by Django 4.0.6 on 2022-12-19 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_alter_student_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='final_list_submitted',
            field=models.BooleanField(default=False),
        ),
    ]
