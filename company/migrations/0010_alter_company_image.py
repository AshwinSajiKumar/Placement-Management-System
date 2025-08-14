# Generated manually to fix Pillow dependency issue

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_alter_company_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='company_images'),
        ),
    ] 