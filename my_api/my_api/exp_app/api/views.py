from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import CarSerializer
from exp_app.models import Car

class CarAPIView(APIView):
  serializer_class = CarSerializer

  def get_queryset(self):
    return Car.objects.all()

  def get(self, request, *args, **kwargs):
    cars = self.get_queryset()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)
  
  def post(self, request, *args, **kwargs):
    car_data = request.data
    new_car = Car.objects.create(car_brand=car_data['car_brand'], car_model=car_data['car_model'],
                car_body=car_data['car_body'], production_year=car_data['production_year'], engine_type=car_data['engine_type'])

    new_car.save()
    serializer = CarSerializer(new_car)
    return Response(serializer.data)
    