import math
from multiprocessing import context
from unittest import result

from django.shortcuts import render

# Create your views here.
from django.views import View
class Home(View):
    def get(self,request):
        return render(request,'home.html')

class Add(View):
    def get(self,request):
        return render(request,'add.html')

    def post(self,request):
        data=request.POST
        n1=int(data['num1'])
        n2=int(data['num2'])

        result=n1+n2

        context={'result':result}

        return render(request,'add.html',context)

class Factorial(View):
    def get(self,request):
        return render(request,'factorial.html')

    def post(self,request):
        data=request.POST
        num = int(data['num'])
        fact=1
        for i in range(1,num+1):
            fact=fact*i

        context = {'fact': fact}

        return render(request, 'factorial.html', context)

class BMI(View):
    def get(self,request):
        return render(request,'bmi.html')

    def post(self,request):
        data=request.POST
        weight=int(data['weight'])
        height = int(data['height'])

        bmi=weight/(height*height)

        context={'bmi':bmi}

        return render(request,'bmi.html',context)





