# Generated by Django 3.0.8 on 2020-10-13 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('System', '0002_auto_20201013_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificates',
            name='Cerificate',
            field=models.ImageField(null=True, upload_to='certificates'),
        ),
        migrations.AlterField(
            model_name='certificates',
            name='Barcode',
            field=models.ImageField(null=True, upload_to='barcodes'),
        ),
    ]