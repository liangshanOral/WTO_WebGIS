# Generated by Django 4.2.8 on 2023-12-21 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wto", "0003_trademonthdata_e_trademonthdata_i_tradequarterdata_e_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="trademonthdata_e",
            name="month",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="trademonthdata_i",
            name="month",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="tradequarterdata_e",
            name="Quarter",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="tradequarterdata_i",
            name="Quarter",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
