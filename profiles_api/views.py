from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API VIEW"""
     
    def get(self, request, format=None):
        """returns list of API view features"""
        an_apiview = [
            'Uses HTTP methods as function',
            'Is similar to traditional django view',
            'gives you the most control over app logic',
            'mapped manually to URLs'
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})
        