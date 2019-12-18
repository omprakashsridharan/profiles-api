from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers, models, permissions
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication


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
        return Response({'message':'Hello','an_apivieew':an_apiview})

    def post(self,request):
        """Create hello message with name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({message:message}) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class HelloViewSet(viewsets.ViewSet):
    """Test API view sets"""

    def list(self,request):
        """List any data"""
        sample_list = ["a","b","c"]
        return Response({'message':'hello','data':sample_list})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)