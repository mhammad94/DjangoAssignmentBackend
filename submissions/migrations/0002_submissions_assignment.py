# Generated by Django 3.1.4 on 2023-02-12 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0001_initial'),
        ('submissions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissions',
            name='assignment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='assignments.assignments'),
        ),
    ]