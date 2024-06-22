# Generated by Django 5.0.3 on 2024-06-17 18:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContentKL', '0004_alter_subjects_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtopic',
            name='Class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ContentKL.classes'),
        ),
        migrations.AlterField(
            model_name='topics',
            name='Class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ContentKL.classes'),
        ),
    ]
