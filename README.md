# Incentive Program Payments to Eligible Hospitals API
This is a REST API implemented in Django. It provides endpoints to retrieve,
create, delete, patch, and put information about incentive program payments to
eligible hospitals. The data included in the project was sourced from [here](https://healthdata.gov/dataset/electronic-health-record-ehr-incentive-program-payments-eligible-hospitals).

## Running the application with Docker
After installing Docker you may run
`docker-compose up`
from the base directory.
It will build the necessary image and start a container.
The app will be running on `localhost:8000`

At this point you may run unit tests:
`docker-compose exec service python manage.py test`

## API
In order to retrieve all imported payments, the endpoint

`api/payments/` may be accessed with a `GET` request.
It will return all the available records in a list:

```
[
    {
        "fid": 1,
        "provider_name": "Sutter Bay Hospitals",
        "npi": 1659439834,
        "ccn": 50008,
        "medicaid_ep_hospital_type": "Acute Care Hospitals",
        "street_address": "CASTRO & DUBOCE STS",
        "city": "SAN FRANCISCO",
        "county": "San Francisco",
        "state": "CA",
        "zip_code": "94114",
        "payment_year_number": 3,
        "program_type": "Medicare/Medicaid",
        "total_payments": 638474,
        "last_program_year": 2015,
        "last_payment_year": 2017,
        "last_payment_criteria": "MU",
        "most_recent_disbursement_amount": 70942,
        "longitude": "-122.435802",
        "latitude": "37.769062"
    },
    ...
    {
        "fid": 328,
        "provider_name": "KAISER FOUNDATION HOSPITALS",
        "npi": 1336294040,
        "ccn": 50411,
        "medicaid_ep_hospital_type": "Acute Care Hospitals",
        "street_address": "25825 S VERMONT AVE",
        "city": "HARBOR CITY",
        "county": "Los Angeles",
        "state": "CA",
        "zip_code": "90710",
        "payment_year_number": 2,
        "program_type": "Medicare/Medicaid",
        "total_payments": 358649,
        "last_program_year": 2016,
        "last_payment_year": 2018,
        "last_payment_criteria": "MU",
        "most_recent_disbursement_amount": 134493,
        "longitude": "-118.294040",
        "latitude": "33.788973"
    }
]
```

In order to retrieve a specific record, make a `GET` request to

`api/payments/{fid}/` where `fid` is the `fid` for the desired record.

For example `api/payments/1/` will return:

```
{
    "fid": 1,
    "provider_name": "Sutter Bay Hospitals",
    "npi": 1659439834,
    "ccn": 50008,
    "medicaid_ep_hospital_type": "Acute Care Hospitals",
    "street_address": "CASTRO & DUBOCE STS",
    "city": "SAN FRANCISCO",
    "county": "San Francisco",
    "state": "CA",
    "zip_code": "94114",
    "payment_year_number": 3,
    "program_type": "Medicare/Medicaid",
    "total_payments": 638474,
    "last_program_year": 2015,
    "last_payment_year": 2017,
    "last_payment_criteria": "MU",
    "most_recent_disbursement_amount": 70942,
    "longitude": "-122.435802",
    "latitude": "37.769062"
}
```

`PATCH`, `PUT`, and `DELETE` are also available under `api/payments/{fid}`

A Payment record may be created by making a `POST` request to `api/payments/`
The available fields are illustrated above in the data retrieval example.
The only required field is `fid` which is used as a unique identifier for the
record.

Some fields go through additional validation.
Failing this validation, such as providing an invalid `latitude`, will result
in a 400 response with the appropriate error message.
