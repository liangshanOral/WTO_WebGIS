# Generated by Django 4.2.8 on 2023-12-21 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wto", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trademonthdata",
            name="export_value_m",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=14, null=True
            ),
        ),
        migrations.AlterField(
            model_name="trademonthdata",
            name="import_value_m",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=14, null=True
            ),
        ),
        migrations.AlterField(
            model_name="tradequarterdata",
            name="export_value_q",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=14, null=True
            ),
        ),
        migrations.AlterField(
            model_name="tradequarterdata",
            name="import_value_q",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=14, null=True
            ),
        ),
        migrations.AlterField(
            model_name="tradeyeardata",
            name="export_value_y",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=14, null=True
            ),
        ),
        migrations.AlterField(
            model_name="tradeyeardata",
            name="import_value_y",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=14, null=True
            ),
        ),
        migrations.AlterField(
            model_name="tradeyearindex",
            name="export_value_i",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=14, null=True
            ),
        ),
        migrations.AlterField(
            model_name="tradeyearindex",
            name="import_value_i",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=14, null=True
            ),
        ),
    ]
