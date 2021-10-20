from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from incentive_program.views import PaymentsViewSet


router = DefaultRouter()
router.register(r'payments', PaymentsViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls))
]
