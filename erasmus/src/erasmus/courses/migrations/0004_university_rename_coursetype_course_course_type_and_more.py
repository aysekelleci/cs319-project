# Generated by Django 4.0.6 on 2022-12-15 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('lowest_grade', models.CharField(max_length=20)),
                ('highest_grade', models.CharField(max_length=20)),
                ('passing_grade', models.CharField(max_length=20)),
                ('inverted_scale', models.BooleanField(default=False)),
                ('department', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='course',
            old_name='courseType',
            new_name='course_type',
        ),
        migrations.AddField(
            model_name='course',
            name='bilkent_equivalent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.course'),
        ),
        migrations.AddField(
            model_name='course',
            name='is_merged',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='MergedCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_type', models.CharField(max_length=30)),
                ('bilkent_equivalent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='merged_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.mergedcourse'),
        ),
        migrations.AddField(
            model_name='course',
            name='university',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.university'),
        ),
    ]
