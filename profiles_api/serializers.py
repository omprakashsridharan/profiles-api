from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serialises name field for testing API view"""

    name = serializers.CharField(max_length=10)
    