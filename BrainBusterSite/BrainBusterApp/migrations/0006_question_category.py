# Generated by Django 5.0.3 on 2024-03-23 10:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BrainBusterApp', '0005_remove_question_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='Category',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.SET_DEFAULT, to='BrainBusterApp.category'),
        ),
    ]
