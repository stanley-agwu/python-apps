from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import viewsets

from my_app.models import CarSpecification
from .serializer import CarSpecificationSerializer

class CarSpecificationViewset(viewsets.ModelViewSet):
    serializer_class = CarSpecificationSerializer
    queryset = CarSpecification.objects.all()