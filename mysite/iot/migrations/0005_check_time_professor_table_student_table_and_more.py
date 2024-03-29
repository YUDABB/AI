# Generated by Django 4.1.1 on 2022-12-02 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("iot", "0004_remove_iot_iot_manager_delete_iot_professor_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="check_time",
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
                ("student_id", models.IntegerField()),
                ("face_id", models.IntegerField()),
                ("pfr", models.IntegerField()),
                ("c_date", models.DateTimeField()),
                ("out_times", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="professor_table",
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
                ("professor_name", models.CharField(max_length=200)),
                ("subject_id", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="student_table",
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
                ("student_name", models.CharField(max_length=200)),
                ("subject_id", models.IntegerField()),
                ("student_count", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="subject_table",
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
                ("subject_id", models.IntegerField()),
                ("subject_name", models.CharField(max_length=200)),
                ("professor_id", models.IntegerField()),
                ("total_time", models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(name="Iot_professors",),
        migrations.AddField(
            model_name="student_table",
            name="student_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="iot.subject_table"
            ),
        ),
        migrations.AddField(
            model_name="professor_table",
            name="professor_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="iot.subject_table"
            ),
        ),
    ]
