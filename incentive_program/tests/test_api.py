from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from incentive_program.models import Payments


class PaymentsTestCase(APITestCase):
	def setUp(self):
		self.payment = Payments.objects.create(fid=282)

	def test_create_payment(self):
		"""
		Test Payment creation via POST.
		"""
		data = {
			'city': 'AUSTIN',
			'npi': 13362,
			'last_program_year': 2019,
			'total_payments': 358,
			'program_type': 'Medicare/Medicaid',
			'payment_year_number': 3,
			'longitude': '-97.742819',
			'most_recent_disbursement_amount': 394,
			'county': 'Travis',
			'last_payment_year': 2019,
			'state': 'TX',
			'ccn': 50411,
			'last_payment_criteria': 'MU',
			'fid': 525,
			'latitude': '30.268091',
			'medicaid_ep_hospital_type': 'Acute Care Hospitals',
			'provider_name': 'TEST HOSPITALS',
			'street_address': '25825 N LAMAR BLVD',
			'zip_code': '78759'
		}
		url = reverse('payments-list')
		response = self.client.post(url, data, format='json')

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Payments.objects.count(), 2)
		self.assertEqual(response.data, data)
		self.assertTrue(Payments.objects.filter(fid=data['fid']).exists())

	def test_create_invalid_payment(self):
		"""
		Test invalid Payment creation via POST by passing invalid data.
		"""
		data = {
			'fid': 823,
			'last_payment_criteria': 'bad_criteria',
		}
		url = reverse('payments-list')
		response = self.client.post(url, data, format='json')

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_delete_payment(self):
		"""
		Test Payments deletion via DELETE.
		"""
		url = reverse('payments-detail', args=[self.payment.fid])
		response = self.client.delete(url, format='json')

		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
		self.assertFalse(
			Payments.objects.filter(fid=self.payment.fid).exists()
		)

	def test_update_payment(self):
		"""
		Test Payment update via PATCH.
		"""
		data = {
			'zip_code': '78701',
			'provider_name': 'Great Hospital',
		}
		url = reverse('payments-detail', args=[self.payment.fid])
		response = self.client.patch(url, data=data, format='json')

		# Refetch payment from database as it has changed.
		self.payment.refresh_from_db()
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(self.payment.zip_code, data['zip_code'])
		self.assertEqual(self.payment.provider_name, data['provider_name'])
