# Generated by Django 4.1.1 on 2022-12-02 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("iot", "0008_alter_student_tables_student_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subject_tables",
            name="professor_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]