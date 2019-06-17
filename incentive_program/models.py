from __future__ import unicode_literals

from django.db import models


class Payments(models.Model):
    ACUTE_CARE_HOSPITALS = 'Acute Care Hospitals'
    CHILDRENS_HOSPITALS = 'Children\'s Hospitals'
    HOSPITAL_TYPE_CHOICES =(
        (ACUTE_CARE_HOSPITALS, ACUTE_CARE_HOSPITALS),
        (CHILDRENS_HOSPITALS, CHILDRENS_HOSPITALS),
    )
    MEDICARE_MEDICAID = 'Medicare/Medicaid'
    MEDICAID = 'Medicaid'
    PROGRAM_TYPE_CHOICES = (
        (MEDICAID, MEDICAID),
        (MEDICARE_MEDICAID, MEDICARE_MEDICAID),
    )
    MU_CRITERIA = 'MU'
    AIU_CRITERIA = 'AIU'
    LAST_PAYMENT_CRITERIA_CHOICES = (
        (AIU_CRITERIA, AIU_CRITERIA),
        (MU_CRITERIA, MU_CRITERIA),
    )

    fid = models.IntegerField(
        primary_key=True,
        db_column='FID',
    )
    provider_name = models.CharField(
        db_column='Provider_Name',
        max_length=256,
        blank=True,
        null=True,
    )
    npi = models.IntegerField(db_column='NPI', blank=True, null=True)
    ccn = models.IntegerField(db_column='CCN', blank=True, null=True)
    medicaid_ep_hospital_type = models.CharField(
        db_column='Medicaid_EP_Hospital_Type',
        choices=HOSPITAL_TYPE_CHOICES,
        max_length=256,
        blank=True,
        null=True,
    )
    street_address = models.CharField(
        db_column='Street_Address',
        max_length=256,
        blank=True,
        null=True,
    )
    city = models.CharField(
        db_column='City',
        max_length=256,
        blank=True,
        null=True,
    )
    county = models.CharField(
        db_column='County',
        max_length=256,
        blank=True,
        null=True,
    )
    state = models.CharField(
        db_column='State',
        max_length=256,
        blank=True,
        null=True,
    )
    zip_code = models.CharField(
        db_column='Zip_Code',
        max_length=5,
        blank=True,
        null=True,
    )
    payment_year_number = models.IntegerField(
        db_column='Payment_Year_Number',
        blank=True,
        null=True,
    )
    program_type = models.CharField(
        db_column='Program_Type',
        choices=PROGRAM_TYPE_CHOICES,
        max_length=256,
        blank=True,
        null=True,
    )
    total_payments = models.IntegerField(
        db_column='Total_payments',
        blank=True,
        null=True,
    )
    last_program_year = models.IntegerField(
        db_column='Last_Program_Year',
        blank=True,
        null=True,
    )
    last_payment_year = models.IntegerField(
        db_column='Last_Payment_Year',
        blank=True, 
        null=True,
    )
    last_payment_criteria = models.CharField(
        db_column='Last_Payment_Criteria',
        choices=LAST_PAYMENT_CRITERIA_CHOICES,
        max_length=256,
        blank=True,
        null=True,
    )
    most_recent_disbursement_amount = models.IntegerField(
        db_column='Most_Recent_Disbursement_Amount',
        blank=True,
        null=True,
    )
    longitude = models.DecimalField(
        db_column='LONGITUDE',
        blank=True,
        null=True,
        max_digits=9,
        decimal_places=6,
    )
    latitude = models.DecimalField(
        db_column='LATITUDE',
        blank=True,
        null=True,
        max_digits=9,
        decimal_places=6,
    )

    class Meta:
        db_table = 'payments'
