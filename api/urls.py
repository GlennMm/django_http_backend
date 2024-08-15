from rest_framework import routers
from .viewsets import PersonViewset

router = routers.DefaultRouter()

router.register(r"people", PersonViewset, basename="person")

urlpatterns = router.urls
