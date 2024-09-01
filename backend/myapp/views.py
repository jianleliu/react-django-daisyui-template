# myapp/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import MyApp
from .serializers import MyAppSerializer


class MyAppViewSet(ModelViewSet):
    queryset = MyApp.objects.all()
    serializer_class = MyAppSerializer

    def list(self, request, *args, **kwargs):
        """Overrides default function to return get response. Use serializer if proccessing django model.

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        sample_data = [
            {
                'id': 1,
                'item': 'integration test',
                'description': 'django backend integrated with react frontend.',
            }
        ]
        return Response(sample_data, status=status.HTTP_200_OK)
