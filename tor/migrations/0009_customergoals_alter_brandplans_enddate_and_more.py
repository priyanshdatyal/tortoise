# Generated by Django 4.0.5 on 2022-07-02 04:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tor', '0008_brandplans_htype_brandplans_ltype_brandplans_mtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerGoals',
            fields=[
                ('userid', models.CharField(max_length=50, primary_key=b'I01\n', serialize=False)),
                ('planid', models.CharField(max_length=50)),
                ('userName', models.CharField(max_length=50)),
                ('selectedAmount', models.CharField(max_length=50)),
                ('selectedTenure', models.CharField(max_length=50)),
                ('startedDate', models.CharField(default=datetime.date(2122, 7, 2), max_length=50)),
                ('depositedAmount', models.CharField(max_length=50)),
                ('benefitPercentage', models.CharField(max_length=50)),
                ('benefitType', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='brandplans',
            name='endDate',
            field=models.DateField(default=datetime.date(2122, 7, 2), max_length=50),
        ),
        migrations.AlterField(
            model_name='brandplans',
            name='quota',
            field=models.CharField(default=10000000000000, max_length=50),
        ),
    ]