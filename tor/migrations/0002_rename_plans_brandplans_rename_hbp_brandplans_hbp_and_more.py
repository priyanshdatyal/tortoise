# Generated by Django 4.0.5 on 2022-06-28 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tor', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Plans',
            new_name='BrandPlans',
        ),
        migrations.RenameField(
            model_name='brandplans',
            old_name='Hbp',
            new_name='hbp',
        ),
        migrations.RenameField(
            model_name='brandplans',
            old_name='higham',
            new_name='hiam',
        ),
    ]