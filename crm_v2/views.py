from django.shortcuts import render

# Create your views here.
from crm.models import Employee
from crm_v2.serializers import EmployeeSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

class EmployeeListCreateView(APIView):

    def get(self,request):

        qs = Employee.objects.all() #qs => PYNT 

        serializer_instance = EmployeeSerializer(qs,many=True)

        return Response(serializer_instance.data)

    def post(self,request):

        form_data = request.data

        # pynt=>qs
        serializer_instance = EmployeeSerializer(data=form_data)

        if serializer_instance.is_valid():

            qs = Employee.objects.create(**form_data)

            serializer_instance = EmployeeSerializer(qs)           

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)



class EmployeeRetrieveUpdateDeleteView(APIView):

    def get(self,request,pk=None):

        qs = Employee.objects.get(id=pk)

        serializer_instance = EmployeeSerializer(qs)

        return Response(serializer_instance.data)

    def put(self,request,pk=None):

        form_data = request.data

        serialier_instance = EmployeeSerializer(data=form_data)

        if serialier_instance.is_valid():

           qs = Employee.objects.filter(id=pk).update(**form_data)

           serializer_instance = EmployeeSerializer(qs)

           return Response(serialier_instance.data)

        else:
            return Response(serialier_instance.errors)


    