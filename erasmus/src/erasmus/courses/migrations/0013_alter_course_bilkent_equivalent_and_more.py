# Generated by Django 4.0.6 on 2022-12-18 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_remove_mergedcourse_course_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='bilkent_equivalent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.bilkentcourse'),
        ),
        migrations.AlterField(
            model_name='mergedcourse',
            name='bilkent_equivalent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.bilkentcourse'),
        ),
    ]
