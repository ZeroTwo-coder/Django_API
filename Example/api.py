from rest_framework import viewsets, permissions

from Example.models import Example
from Example.serializers import ExampleSerializer


class ExampleViewSet(viewsets.ModelViewSet):
    queryset = Example.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ExampleSerializer
