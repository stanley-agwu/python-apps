from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import CarSerializer
from exp_app.models import Car

class CarAPIView(APIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return Car.objects.all()

    def get(self, request, *args, **kwargs):
        print(request.query_params)
        try:
            id = request.query_params['id']
            if (id != None):
                cars = Car.objects.get(id=id)
            serializer = CarSerializer(cars)
        except:
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

    def put(self, request, *args, **kwargs):
        # id = request.query_params["id"]
        car_obj = Car.objects.get()

        data = request.data

        car_obj.car_brand = data['car_brand']
        car_obj.car_model = data['car_model']
        car_obj.car_body = data['car_body']
        car_obj.engine_type = data['engine_type']
        car_obj.production_year = data['production_year']

        car_obj.save()

        serializer = CarSerializer(car_obj)

        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        car_object = Car.objects.get()
        data = request.data

        car_object.car_brand = data.get("car_brand", car_object.car_brand)
        car_object.car_model = data.get("car_model", car_object.car_model)
        car_object.production_year = data.get("production_year", car_object.production_year)
        car_object.car_body = data.get("car_body", car_object.car_body)
        car_object.engine_type = data.get("engine_type", car_object.engine_type)

        car_object.save()
        serializer = CarSerializer(car_object)

        return Response(serializer.data)