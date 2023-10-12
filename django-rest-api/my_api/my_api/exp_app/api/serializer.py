from rest_framework import serializers
from exp_app.models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'car_brand', 'car_model', 'engine_type',
                    'car_body', 'production_year']
        extra_kwargs = {
            'id': {'read_only': True},
        }