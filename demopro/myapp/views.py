# from django.contrib.admindocs.utils import name
from django.db.models import Model
from django.shortcuts import render
from django.template.backends import django
from django.utils.decorators import method_decorator

# Create your views here.
from django.views import View
from django.http import HttpResponse,JsonResponse

class Goodmorning(View):
    def get(self,request):
        data={"Message":"Good Morning"}
        return JsonResponse(data)


class Helloworld(View):
    def get(self,request):
        data = {"Message": "Hello World"}
        return JsonResponse(data)

class Goodevening(View):
    def get(self,request):
        data={"Message":"Good Evening"}
        return JsonResponse(data)

class UserDetails(View):
    def get(self,request):
        data=[
            {'name':"Arun",'age':23,'place':'ekm'},
            {'name': "Amal", 'age': 24, 'place': 'tvm'},
            {'name': "Anu", 'age': 25, 'place': 'ekm'}
        ]

        return JsonResponse(data,self=False)

#API view for reading all student records
from myapp.models import Student
class StudentList(View):
    def get(self,request):

        s=Student.objects.all().values()
        print(s)
        print(type(s))

        data=list(s)
        print(data)
        print(type(data))

        return JsonResponse(data,safe=False)

#API view for creating a new student record
from json import loads
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
@method_decorator(csrf_exempt,name="dispatch")
class Studentcreate(View):
    def post(self,request):
        data=loads(request.body)

        r=data['rollno']
        n=data['name']
        a=data['age']
        p=data['place']
        m=data['marks']

        s=Student.objects.create(rollno=r,name=n,age=a,place=p,marks=m)
        s.save()

        return JsonResponse({"message":"Inserted data successfully"})

class StudentDetail(View):
    def get(self,request,i):
        s=list(Student.objects.filter(id=i).values())
        if s:
            return JsonResponse(s,safe=False)
        else:
            return JsonResponse({"message":"No student data"})

@method_decorator(csrf_exempt,name="dispatch")
class StudentDelete(View):
    def delete(self,request,i):
        s=Student.objects.get(id=i)
        s.delete()
        return JsonResponse({"message":"Deleted Successfully"})


import json

@method_decorator(csrf_exempt,name="dispatch")
class Studentfullupdate(View):
    def put(self,request,i):
        data = json.loads(request.body)
        print(data)

        s=Student.objects.get(id=i)
        s.rollno = data['rollno']
        s.name =data['name']
        s.age = data['age']
        s.place = data['place']
        s.marks =data['marks']
        s.save()
        return JsonResponse({"message":"updated Successfully"})


@method_decorator(csrf_exempt,name="dispatch")
class Studentpartalupdate(View):
    def patch(self,request,i):
        data = json.loads(request.body)
        print(data)

        s=Student.objects.get(id=i)
        if 'rollno' in data :
            s.rollno= data['name']
        if 'name' in data:
            s.name =data['name']
        if 'age' in data:
            s.age = data['age']
        if 'place' in data:
            s.place = data['place']
        if 'marks' in data:
            s.marks =data['marks']
        s.save()
        return JsonResponse({"message":"updated partally"})

