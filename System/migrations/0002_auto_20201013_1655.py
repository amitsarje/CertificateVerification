# Generated by Django 3.0.8 on 2020-10-13 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('System', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='Students',
        ),
        migrations.AddField(
            model_name='certificates',
            name='Student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='System.Students'),
        ),
    ]