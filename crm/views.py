from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from crm.models import Employee
from json import loads


@method_decorator(csrf_exempt,name="dispatch")
class EmployeeListCreateView(View):

    def get(self,request):

        qs = Employee.objects.all().values() #qs

        response_data = list(qs) #qs=>pynt

        return JsonResponse(response_data,safe=False) # pynt => json

    def post(self,request):

        json_data = request.body

        form_data = loads(json_data)       

        # Employee.objects.create(
        #         name=form_data.get("name"),
        #         email=form_data.get("email"),
        #         phone=form_data.get("phone"),
        #         salary=form_data.get("salary"),
        #         department=form_data.get("department"),
        #         location=form_data.get("location")                
        #         )

        Employee.objects.create(**form_data)

        response_data = {"message":"employee created"}

        return JsonResponse(response_data)


@method_decorator(csrf_exempt,name="dispatch")
class EmployeeRetrieveUpdateDeleteView(View):

    def get(self,request,pk=None):

        qs = Employee.objects.filter(id=pk).values()

        response_data = list(qs)

        return JsonResponse(response_data,safe=False)

    def put(self,request,pk=None):

        json_data = request.body

        form_data = loads(json_data)

        Employee.objects.filter(id=pk).update(**form_data)

        respon_data = {"message":"updated"}

        return JsonResponse(respon_data)

    def delete(self,request,pk=None):

        Employee.objects.filter(id=pk).delete()

        response_data = {"message":"deleted"}

        return JsonResponse(response_data) 
    
