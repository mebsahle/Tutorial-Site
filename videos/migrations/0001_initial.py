# Generated by Django 2.2.9 on 2020-04-29 20:13

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
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200)),
                ('course_description', models.CharField(max_length=200)),
                ('course_created_at', models.DateTimeField(auto_now=True)),
                ('course_code', models.CharField(help_text='eg. CSE0000', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=200)),
                ('department_description', models.CharField(max_length=200)),
                ('department_created_at', models.DateTimeField(auto_now=True)),
                ('department_short_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Department',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=200)),
                ('video_file', models.FileField(default='null', upload_to='videos/uploads/')),
                ('publication_date', models.DateTimeField(auto_now=True)),
                ('course_code', models.ForeignKey(default='C', on_delete=django.db.models.deletion.CASCADE, to='videos.Course')),
                ('published_by', models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, related_name='published', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Videos',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='department_short_name',
            field=models.ForeignKey(default='D', on_delete=django.db.models.deletion.CASCADE, to='videos.Department'),
        ),
    ]