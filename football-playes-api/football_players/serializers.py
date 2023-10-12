from rest_framework import serializers
from .models import Player

# Serializers define the API representation.
class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'url', 'first_name', 'last_name', 'football_club', 
        'nationality', 'age', 'position',]