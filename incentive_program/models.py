from __future__ import unicode_literals

from django.db import models


class Payments(models.Model):
    fid = models.TextField(
        primary_key=True,
        db_column='FID',
    )
    x = models.TextField(db_column='X', blank=True, null=True)
    y = models.TextField(db_column='Y', blank=True, null=True)
    provider_name = models.TextField(
        db_column='Provider_Name',
        blank=True,
        null=True,
    )
    npi = models.TextField(db_column='NPI', blank=True, null=True)
    ccn = models.TextField(db_column='CCN', blank=True, null=True)
    medicaid_ep_hospital_type = models.TextField(
        db_column='Medicaid_EP_Hospital_Type',
        blank=True,
        null=True,
    )
    street_address = models.TextField(
        db_column='Street_Address',
        blank=True,
        null=True,
    )
    city = models.TextField(db_column='City', blank=True, null=True)
    county = models.TextField(db_column='County', blank=True, null=True)
    state = models.TextField(db_column='State', blank=True, null=True)
    zip_code = models.TextField(db_column='Zip_Code', blank=True, null=True)
    payment_year_number = models.TextField(
        db_column='Payment_Year_Number',
        blank=True,
        null=True,
    )
    program_type = models.TextField(
        db_column='Program_Type',
        blank=True,
        null=True,
    )
    total_payments = models.TextField(
        db_column='Total_payments',
        blank=True,
        null=True,
    )
    last_program_year = models.TextField(
        db_column='Last_Program_Year',
        blank=True,
        null=True,
    )
    last_payment_year = models.TextField(
        db_column='Last_Payment_Year',
        blank=True, 
        null=True,
    )
    last_payment_criteria = models.TextField(
        db_column='Last_Payment_Criteria',
        blank=True,
        null=True,
    )
    most_recent_disbursement_amount = models.TextField(
        db_column='Most_Recent_Disbursement_Amount',
        blank=True,
        null=True,
    )
    longitude = models.TextField(db_column='LONGITUDE', blank=True, null=True)
    latitude = models.TextField(db_column='LATITUDE', blank=True, null=True)

    class Meta:
        db_table = 'payments'
