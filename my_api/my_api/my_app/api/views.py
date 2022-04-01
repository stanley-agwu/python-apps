from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import viewsets

from my_app.models import CarSpecification
from .serializer import CarSpecificationSerializer

class CarSpecificationViewset(viewsets.ModelViewSet):
    serializer_class = CarSpecificationSerializer
    queryset = CarSpecification.objects.all()

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        params_list = params['pk'].split('-')
        cars = CarSpecification.objects.all().filter(car_brand=params_list[0], car_model=params_list[1])
        serializer = CarSpecificationSerializer(cars, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        car_data = request.data
        new_car = CarSpecification.objects.create(car_brand=car_data['car_brand'], car_model=car_data['car_model'],
                    car_body=car_data['car_body'], production_year=car_data['production_year'], engine_type=car_data['engine_type'])

        new_car.save()
        serializer = CarSpecificationSerializer(new_car)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        car = self.get_object()
        car.delete()

        return Response({'message': car.car_model + ' deleted successfully!'})