# Generated by Django 2.1.2 on 2018-10-12 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstract_base_classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]