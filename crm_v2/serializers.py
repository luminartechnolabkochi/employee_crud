
from rest_framework import serializers

class EmployeeSerializer(serializers.Serializer):

    name = serializers.CharField()

    email = serializers.EmailField() 

    phone = serializers.CharField()

    salary = serializers.DecimalField(max_digits=10,decimal_places=2)

    department = serializers.CharField()

    location = serializers.CharField()





