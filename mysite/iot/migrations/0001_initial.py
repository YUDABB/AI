# Generated by Django 4.1.1 on 2022-09-18 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Iot_Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Iot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part', models.CharField(max_length=200)),
                ('data', models.IntegerField()),
                ('create_date', models.DateTimeField()),
                ('iot_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iot.iot_manager')),
            ],
        ),
    ]