# Generated by Django 4.2.2 on 2023-06-28 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='company_images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slots', models.IntegerField()),
                ('role', models.CharField(max_length=30)),
                ('cgpa', models.IntegerField()),
                ('Backpaper', models.IntegerField()),
                ('Lpa', models.IntegerField()),
                ('internship', models.IntegerField()),
                ('tech', models.CharField(max_length=30)),
                ('City', models.CharField(max_length=20)),
                ('Country', models.CharField(max_length=20)),
                ('tenthper', models.IntegerField()),
                ('twelthper', models.IntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.job')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.student')),
            ],
        ),
    ]