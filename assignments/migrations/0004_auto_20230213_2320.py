# Generated by Django 3.1.4 on 2023-02-13 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20230213_0154'),
        ('assignments', '0003_auto_20230213_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignments',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courses.courses'),
        ),
    ]
