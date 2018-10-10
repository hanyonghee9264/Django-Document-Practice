# Generated by Django 2.1.2 on 2018-10-09 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foreignkey', '0002_fcuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fcuser',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='foreignkey.FCUser'),
        ),
    ]