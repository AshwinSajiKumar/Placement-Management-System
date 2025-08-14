# Generated manually to fix Pillow dependency issue

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_remove_student_import_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='student_images'),
        ),
    ] 