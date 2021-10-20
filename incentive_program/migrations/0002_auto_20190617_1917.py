# -*- coding: utf-8 -*-
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incentive_program', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payments',
            name='x',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='y',
        ),
        migrations.AlterField(
            model_name='payments',
            name='ccn',
            field=models.IntegerField(null=True, db_column='CCN', blank=True),
        ),
        migrations.AlterField(
            model_name='payments',
            name='city',
            field=models.CharField(max_length=256, null=True, db_column='City', blank=True),
        ),
        migrations.AlterField(
            model_name='payments',
            name='county',
            field=models.CharField(max_length=256, null=True, db_column='County', blank=True),
        ),
        migrations.AlterField(
            model_name='payments',
            name='fid',
            field=models.IntegerField(serialize=False, primary_key=True, db_column='FID'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='last_payment_criteria',
            field=models.CharField(blank=True, max_length=256, null=True, db_column='Last_Payment_Criteria', choices=[('AIU', 'AIU'), ('MU', 'MU')]),
        ),
        migrations.AlterField(
            model_name='payments',
            name='last_payment_year',
            field=models.IntegerField(null=True, db_column='Last_Payment_Year', blank=True),
        ),
        migrations.AlterField(
            model_name='payments',
            name='last_program_year',
            field=models.IntegerField(null=True, db_column='Last_Program_Year', blank=True),
        ),
        migrations.AlterField(
            model_name='payments',
            name='latitude',
            field=models.DecimalField(null=True, decimal_places=6, max_digits=9, db_column='LATITUDE', blank=True),
        ),
        migrations.AlterField(
            model_name='payments',
            name='longitude',
            field=models.DecimalField(null=True, decimal_places=6, max_digits=9, db_column='LONGITUDE', blank=True),
        ),
        migrations.AlterField(
            model_name='payments',
            name='medicaid_ep_hospital_type',
            field=models.CharField(blank=True, max_length=256, null=True, db_column='Medicaid_EP_Hospital_Type', choices=[('Acute Care Hospitals', 'Acute Care Hospitals'), ("Children's Hospitals", "Children's Hospitals")]),
        ),
        migrations.AlterField(
            model_name='payments',
            name='most_recent_disbursement_amount',
            field=models.IntegerField(null=True, db_column='Most_Recent_Disbursement_Amount', blank=True),
        ),
        migrations.AlterField(
            model_name='payments',
            name='npi',
            field=models.IntegerField(null=True, db_column='NPI', blank=True),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_year_number',
            field=models.IntegerField(null=True, db_column='Payment_Year_Number', blank=True),
        ),
        migrations.AlterField(
            model_name='payments',
            name='program_type',
            field=models.CharField(blank=True, max_length=256, null=True, db_column='Program_Type', choices=[('Medicaid', 'Medicaid'), ('Medicare/Medicaid', 'Medicare/Medicaid')]),
        ),
        migrations.AlterField(
            model_name='payments',
            name='provider_name',
            field=models.CharField(max_length=256, null=True, db_column='Provider_Name', blank=True),
        ),
        migrations.AlterField(
            model_name='payments',
            name='state',
            field=models.CharField(max_length=256, null=True, db_column='State', blank=True),
        ),
        migrations.AlterField(
            model_name='payments',
            name='street_address',
            field=models.CharField(max_length=256, null=True, db_column='Street_Address', blank=True),
        ),
        migrations.AlterField(
            model_name='payments',
            name='total_payments',
            field=models.IntegerField(null=True, db_column='Total_payments', blank=True),
        ),
        migrations.AlterField(
            model_name='payments',
            name='zip_code',
            field=models.CharField(max_length=5, null=True, db_column='Zip_Code', blank=True),
        ),
    ]
