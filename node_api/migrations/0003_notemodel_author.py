# Generated by Django 5.0.7 on 2024-07-31 18:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node_api', '0002_authormodel_alter_notemodel_updatedat'),
    ]

    operations = [
        migrations.AddField(
            model_name='notemodel',
            name='author',
            field=models.ForeignKey(default='5048a7ef-c13e-46a0-a951-410055dcd558', on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='node_api.authormodel'),
        ),
    ]
