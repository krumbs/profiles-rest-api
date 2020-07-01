from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers


# Create your views here.

class HelloAPIView(APIView):
    """Test API View"""

    # Overwrite serialiser class
    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to a tradional Django view',
            'Gives you the most controle over your logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})


    def post(self, request):
        """Creates a hello message with our name."""

        s = serializers.HelloSerializer(data=request.data)

        # Validate data
        if s.is_valid():
            name = s.data.get('name')
            msg = 'Hello {}'.format(name)
            return Response({'message': msg})
        else:
            return Response(
                s.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Updates an object at primary key"""

        # NOT implemented yet

        return Response({'method': 'put'})


    def patch(self, request, pk=None):
        """Only updates the fields required in the request."""

        # NOT implemented yet

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Deletes an object."""

        # NOT implemented yet

        return Response({'method': 'delete'})
