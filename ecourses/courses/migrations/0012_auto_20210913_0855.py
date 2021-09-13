# Generated by Django 3.2.6 on 2021-09-13 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_course_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='lession',
            new_name='lesson',
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', related_query_name='my_lesson', to='courses.course'),
        ),
    ]
