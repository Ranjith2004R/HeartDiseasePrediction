# Generated by Django 5.1.5 on 2025-01-29 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.FloatField()),
                ('gender', models.IntegerField()),
                ('heart_rate', models.FloatField()),
                ('systolic_bp', models.FloatField()),
                ('diastolic_bp', models.FloatField()),
                ('blood_sugar', models.FloatField()),
                ('ck_mb', models.FloatField()),
                ('troponin', models.FloatField()),
            ],
        ),
    ]
