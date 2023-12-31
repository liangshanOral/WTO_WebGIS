# Generated by Django 4.2.8 on 2023-12-21 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wto", "0002_alter_trademonthdata_export_value_m_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="TradeMonthData_E",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "export_value_m",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=14, null=True
                    ),
                ),
                (
                    "reporting_country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reporting_month_country_e",
                        to="wto.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TradeMonthData_I",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "import_value_m",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=14, null=True
                    ),
                ),
                (
                    "reporting_country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reporting_month_country_i",
                        to="wto.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TradeQuarterData_E",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Quarter", models.IntegerField()),
                (
                    "export_value_q",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=14, null=True
                    ),
                ),
                (
                    "reporting_country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reporting_quarter_country_e",
                        to="wto.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TradeQuarterData_I",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Quarter", models.IntegerField()),
                (
                    "import_value_q",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=14, null=True
                    ),
                ),
                (
                    "reporting_country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reporting_quarter_country_i",
                        to="wto.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TradeYearData_E",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("year", models.IntegerField()),
                (
                    "export_value_y",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=14, null=True
                    ),
                ),
                (
                    "partner_country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="partner_country_e",
                        to="wto.country",
                    ),
                ),
                (
                    "product_sector",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wto.productsector",
                    ),
                ),
                (
                    "reporting_country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reporting_year_country_e",
                        to="wto.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TradeYearData_I",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("year", models.IntegerField()),
                (
                    "import_value_y",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=14, null=True
                    ),
                ),
                (
                    "partner_country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="partner_country_i",
                        to="wto.country",
                    ),
                ),
                (
                    "product_sector",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wto.productsector",
                    ),
                ),
                (
                    "reporting_country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reporting_year_country_i",
                        to="wto.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TradeYearIndex_E",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("year", models.IntegerField()),
                (
                    "export_value_i",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=14, null=True
                    ),
                ),
                (
                    "reporting_country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reporting_index_country_e",
                        to="wto.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TradeYearIndex_I",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("year", models.IntegerField()),
                (
                    "import_value_i",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=14, null=True
                    ),
                ),
                (
                    "reporting_country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reporting_index_country_i",
                        to="wto.country",
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="tradequarterdata",
            name="reporting_country",
        ),
        migrations.RemoveField(
            model_name="tradeyeardata",
            name="partner_country",
        ),
        migrations.RemoveField(
            model_name="tradeyeardata",
            name="product_sector",
        ),
        migrations.RemoveField(
            model_name="tradeyeardata",
            name="reporting_country",
        ),
        migrations.RemoveField(
            model_name="tradeyearindex",
            name="reporting_country",
        ),
        migrations.DeleteModel(
            name="TradeMonthData",
        ),
        migrations.DeleteModel(
            name="TradeQuarterData",
        ),
        migrations.DeleteModel(
            name="TradeYearData",
        ),
        migrations.DeleteModel(
            name="TradeYearIndex",
        ),
    ]
