# Generated by Django 5.0 on 2024-01-02 07:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wto', '0008_commercialdata_e_individual_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSector_MFN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MFN_a',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('MFN_value', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True)),
                ('reporting_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reporting_country_mfn_a', to='wto.country_l')),
            ],
        ),
        migrations.CreateModel(
            name='MFN_b',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('export_value', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True)),
                ('reporting_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reporting_country_mfn_b', to='wto.country_l')),
                ('product_sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wto.productsector_mfn')),
            ],
        ),
    ]
