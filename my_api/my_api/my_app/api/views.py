from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

# class ExampleView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         content = {
#             'status': 'request was permitted'
#         }
#         return Response(content)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

@api_view()
@permission_classes([AllowAny])
def hello_world(request):
    return Response({"message": "Hello, world!"})