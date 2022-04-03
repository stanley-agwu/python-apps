from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import viewsets

from my_app.models import CarSpecification, CarPlan
from .serializer import CarSpecificationSerializer

class CarSpecificationViewset(viewsets.ModelViewSet):
    serializer_class = CarSpecificationSerializer
    queryset = CarSpecification.objects.all()

    # def retrieve(self, request, *args, **kwargs):
    #     params = kwargs
    #     params_list = params['pk'].split('-')
    #     cars = CarSpecification.objects.all().filter(car_brand=params_list[0], car_model=params_list[1])
    #     serializer = CarSpecificationSerializer(cars, many=True)

    #     return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        car_data = request.data
        new_car = CarSpecification.objects.create(car_plan=CarPlan.objects.get(id=car_data['car_plan']), car_brand=car_data['car_brand'], car_model=car_data['car_model'],
                    car_body=car_data['car_body'], production_year=car_data['production_year'], engine_type=car_data['engine_type'])

        new_car.save()
        serializer = CarSpecificationSerializer(new_car)
        return Response(serializer.data)

    # def destroy(self, request, *args, **kwargs):
    #     car = self.get_object()
    #     car.delete()

    #     return Response({'message': car.car_model + ' deleted successfully!'})

    def update(self, request, *args, **kwargs):
        car_object = self.get_object()
        data = request.data

        car_plan = CarPlan.objects.get(plan_name=data['plan_name'])

        car_object.car_plan = car_plan
        car_object.car_brand = data['car_brand']
        car_object.car_model = data['car_model']
        car_object.car_body = data['car_body']
        car_object.engine_type = data['engine_type']
        car_object.production_year = data['production_year']

        car_object.save()
        serializer = CarSpecificationSerializer(car_object)

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        car_object = self.get_object()
        data = request.data

        try:
            car_plan = CarPlan.objects.get(plan_name=data['plan_name'])
            car_object.car_plan = car_plan
        except KeyError:
            pass

        car_object.car_brand = data.get("car_brand", car_object.car_brand)
        car_object.car_model = data.get("car_model", car_object.car_model)
        car_object.production_year = data.get("production_year", car_object.production_year)
        car_object.car_body = data.get("car_body", car_object.car_body)
        car_object.engine_type = data.get("engine_type", car_object.engine_type)

        car_object.save()
        serializer = CarSpecificationSerializer(car_object)

        return Response(serializer.data)