from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer


def drink_list(request, format=None):
    # get all the DrinkSerializer
    # serialize them
    # return json
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return JsonResponse({"drinks": serializer.data})

