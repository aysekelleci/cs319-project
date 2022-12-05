# Generated by Django 4.0.6 on 2022-12-05 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpa', models.FloatField()),
                ('score', models.FloatField()),
                ('status', models.CharField(blank=True, max_length=100)),
                ('is_erasmus_done', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.erasmususer')),
            ],
        ),
        migrations.CreateModel(
            name='Coordinator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.erasmususer')),
            ],
        ),
        migrations.CreateModel(
            name='BoardMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.erasmususer')),
            ],
        ),
    ]
