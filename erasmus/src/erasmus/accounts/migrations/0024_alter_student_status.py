# Generated by Django 4.0.6 on 2022-12-19 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_alter_erasmususer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('Account created', 'Account created'), ('Placement done', 'Placement done'), ('No placement', 'No placement'), ('Choosing courses', 'Choosing courses'), ('Waiting for the course approval', 'Waiting for the course approval'), ('Waiting for the final course list approval', 'Waiting for the final course list approval'), ('Final course list is approved, generate pre-approval form', 'Final course list is approved, generate pre-approval form'), ('Waiting for the pre-approval form to be signed', 'Waiting for the pre-approval form to be signed'), ('Waiting for the mobility period', 'Waiting for the mobility period'), ('In mobility period', 'In mobility period'), ('Finished mobility period', 'Finished mobility period')], default='Account created', max_length=200),
        ),
    ]
