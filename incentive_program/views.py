from rest_framework import viewsets

from incentive_program.models import Payments
from incentive_program.serializers import PaymentsSerializer


class PaymentsViewSet(viewsets.ModelViewSet):
	queryset = Payments.objects.order_by('pk')
	serializer_class = PaymentsSerializer
