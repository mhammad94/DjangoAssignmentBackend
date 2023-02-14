# Generated by Django 3.1.4 on 2023-02-12 22:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0002_auto_20230213_0154'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignmenttitle', models.CharField(default='New Assignment', max_length=250)),
                ('submitted', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='courses.courses')),
                ('submitter', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
