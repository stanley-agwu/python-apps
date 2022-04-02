from rest_framework import serializers
from my_app.models import CarSpecification

class CarSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSpecification
        fields = ['id', 'car_plan', 'car_brand', 'car_model', 'engine_type',
                    'car_body', 'production_year']
        extra_kwargs = {
            'id': {'read_only': True},
        }
        depth = 1