# Generated by Django 4.2.2 on 2023-07-07 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_alter_student_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='import_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]