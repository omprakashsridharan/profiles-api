from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """Test API VIEW"""
    serializer_class = serializers.HelloSerializer
     
    def get(self, request, format=None):
        """returns list of API view features"""
        an_apiview = [
            'Uses HTTP methods as function',
            'Is similar to traditional django view',
            'gives you the most control over app logic',
            'mapped manually to URLs'
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self,request):
        """Create hello message with name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({message:message}) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        