from rest_framework import serializers

from incentive_program.models import Payments


class PaymentsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Payments
		exclude = ()
