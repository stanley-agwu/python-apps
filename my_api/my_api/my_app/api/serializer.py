from rest_framework import serializers
from my_app.models import CarSpecification

class CarSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSpecification
        fields = ['car_brand', 'car_model', 'engine_type','car_body', 'production_year']