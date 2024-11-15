# Generated by Django 4.1.13 on 2024-11-12 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=40)),
                ('taskDescription', models.TextField()),
                ('is_completed', models.BooleanField()),
                ('category', models.ManyToManyField(to='category.taskcategorymodel')),
            ],
        ),
    ]
