# Generated by Django 4.1.6 on 2023-02-11 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursetitle', models.CharField(default='New Course', max_length=250)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
