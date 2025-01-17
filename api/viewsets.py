from rest_framework import viewsets
from .serializers import PersonSerializer
from .models import Person


class PersonViewset(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
