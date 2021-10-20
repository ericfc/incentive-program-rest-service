# -*- coding: utf-8 -*-
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('fid', models.TextField(serialize=False, primary_key=True, db_column='FID')),
                ('x', models.TextField(null=True, db_column='X', blank=True)),
                ('y', models.TextField(null=True, db_column='Y', blank=True)),
                ('provider_name', models.TextField(null=True, db_column='Provider_Name', blank=True)),
                ('npi', models.TextField(null=True, db_column='NPI', blank=True)),
                ('ccn', models.TextField(null=True, db_column='CCN', blank=True)),
                ('medicaid_ep_hospital_type', models.TextField(null=True, db_column='Medicaid_EP_Hospital_Type', blank=True)),
                ('street_address', models.TextField(null=True, db_column='Street_Address', blank=True)),
                ('city', models.TextField(null=True, db_column='City', blank=True)),
                ('county', models.TextField(null=True, db_column='County', blank=True)),
                ('state', models.TextField(null=True, db_column='State', blank=True)),
                ('zip_code', models.TextField(null=True, db_column='Zip_Code', blank=True)),
                ('payment_year_number', models.TextField(null=True, db_column='Payment_Year_Number', blank=True)),
                ('program_type', models.TextField(null=True, db_column='Program_Type', blank=True)),
                ('total_payments', models.TextField(null=True, db_column='Total_payments', blank=True)),
                ('last_program_year', models.TextField(null=True, db_column='Last_Program_Year', blank=True)),
                ('last_payment_year', models.TextField(null=True, db_column='Last_Payment_Year', blank=True)),
                ('last_payment_criteria', models.TextField(null=True, db_column='Last_Payment_Criteria', blank=True)),
                ('most_recent_disbursement_amount', models.TextField(null=True, db_column='Most_Recent_Disbursement_Amount', blank=True)),
                ('longitude', models.TextField(null=True, db_column='LONGITUDE', blank=True)),
                ('latitude', models.TextField(null=True, db_column='LATITUDE', blank=True)),
            ],
            options={
                'db_table': 'payments',
            },
        ),
    ]
