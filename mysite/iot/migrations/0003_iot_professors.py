# Generated by Django 4.1.1 on 2022-12-01 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("iot", "0002_iot_professor"),
    ]

    operations = [
        migrations.CreateModel(
            name="Iot_professors",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("face_id", models.IntegerField()),
                ("professor_id", models.IntegerField()),
                ("curr_date", models.DateTimeField()),
                ("times", models.IntegerField()),
                ("out_times", models.IntegerField()),
            ],
        ),
    ]
