from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework import filters
from rest_framework import status
from rest_framework import viewsets

from . import serializers
from . import models
from . import permissions

# Create your views here.

class HelloAPIView(APIView):
    """Test API View"""

    # Overwrite serialiser class
    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete).',
            'It is similar to a tradional Django view.',
            'Gives you the most controle over your logic.',
            'Is mapped manually to URLs.'
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


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet."""

    # Overwrite serializer class
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Returns a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update).',
            'Automatically maps to URLs using Routers.',
            'Provides more functionality with less code.'
        ]
        return Response({'message': 'Hello.', 'a_viewset': a_viewset})


    def create(self, request):
        """Creates a new hello message."""

        s = serializers.HelloSerializer(data=request.data)

        # Validate data
        if s.is_valid():
            name = s.data.get('name')
            msg = 'Hello {}.'.format(name)
            return Response({'message': msg})
        else:
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        """Gets object by id."""

        # Not implemented yet

        return Response({'http_method': 'GET'})


    def update(self, request, pk=None):
        """HTTP PUT object by id."""

        # Not implemented yet

        return Response({'http_method': 'PUT'})


    def partial_update(self, request, pk=None):
        """HTTP PATCH object by id."""

        # Not implemented yet

        return Response({'http_method': 'PATCH'})


    def destroy(self, request, pk=None):
        """HTTP DELETE object by id."""

        # Not implemented yet

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating"""

    serializer_class = serializers.UserProfileSerializer

    # How to retrieve the objects from the DB
    queryset = models.UserProfile.objects.all()

    # Set the authentication classes tuple
    authentication_classes = (TokenAuthentication,)

    # Set the permissions tuple
    permission_classes = (permissions.UpdateOwnProfile,)

    # Use inbuilt filters
    filter_backends = (filters.SearchFilter,)

    # Specify which fields we want the built-in  filters to be able
    # to search by
    search_fields = ('name', 'email',)



class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Uses the ObtainAuthToken APIView to validate and create a token."""

        return ObtainAuthToken().post(request)
