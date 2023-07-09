# Generated by Django 4.1.1 on 2022-11-30 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professor_name', models.CharField(max_length=200)),
                ('subject', models.TextField()),
                ('professor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
                ('student_id', models.IntegerField()),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_ck.professor')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_names', models.CharField(max_length=200)),
                ('day1a', models.BooleanField(null=True)),
                ('day1b', models.BooleanField(null=True)),
                ('day1c', models.BooleanField(null=True)),
                ('day2a', models.BooleanField(null=True)),
                ('day2b', models.BooleanField(null=True)),
                ('day2c', models.BooleanField(null=True)),
                ('day3a', models.BooleanField(null=True)),
                ('day3b', models.BooleanField(null=True)),
                ('day3c', models.BooleanField(null=True)),
                ('day4a', models.BooleanField(null=True)),
                ('day4b', models.BooleanField(null=True)),
                ('day4c', models.BooleanField(null=True)),
                ('day5a', models.BooleanField(null=True)),
                ('day5b', models.BooleanField(null=True)),
                ('day5c', models.BooleanField(null=True)),
                ('day6a', models.BooleanField(null=True)),
                ('day6b', models.BooleanField(null=True)),
                ('day6c', models.BooleanField(null=True)),
                ('day7a', models.BooleanField(null=True)),
                ('day7b', models.BooleanField(null=True)),
                ('day7c', models.BooleanField(null=True)),
                ('day8a', models.BooleanField(null=True)),
                ('day8b', models.BooleanField(null=True)),
                ('day8c', models.BooleanField(null=True)),
                ('day9a', models.BooleanField(null=True)),
                ('day9b', models.BooleanField(null=True)),
                ('day9c', models.BooleanField(null=True)),
                ('day10a', models.BooleanField(null=True)),
                ('day10b', models.BooleanField(null=True)),
                ('day10c', models.BooleanField(null=True)),
                ('day11a', models.BooleanField(null=True)),
                ('day11b', models.BooleanField(null=True)),
                ('day11c', models.BooleanField(null=True)),
                ('day12a', models.BooleanField(null=True)),
                ('day12b', models.BooleanField(null=True)),
                ('day12c', models.BooleanField(null=True)),
                ('day13a', models.BooleanField(null=True)),
                ('day13b', models.BooleanField(null=True)),
                ('day13c', models.BooleanField(null=True)),
                ('day14a', models.BooleanField(null=True)),
                ('day14b', models.BooleanField(null=True)),
                ('day14c', models.BooleanField(null=True)),
                ('day15a', models.BooleanField(null=True)),
                ('day15b', models.BooleanField(null=True)),
                ('day15c', models.BooleanField(null=True)),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_ck.professor')),
            ],
        ),
    ]
