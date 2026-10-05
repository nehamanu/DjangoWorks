from multiprocessing import context

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def first(request):
#     if(request.method=='GET'):
#         return HttpResponse('First page')
# def second (request):
#     if (request.method == 'GET'):
#         return HttpResponse('Second page')

#class-based
# from django.views import View
# class First(View):
#     def get(self,request):
#         return HttpResponse("""
#         <h1>First page</h1>
#         <h1>hello</h1>""")
from django.views import View

from myapp.models import Person


class First(View):
    def get(self,request):
        # data=[{"name":"Arun","age":23,"place":"ekm"},
        #       {"name":"Amal","age":23,"place":"tvm"},
        #       {"name":"Anu","age":23,"place":"knr"}]

        data=Person.objects.all()
        context={'data':data}
        return render(request,'first.html',context)

# class Second(View):
#     def get(self,request):
#         return HttpResponse("<h1>Second page</h1>")
class Second(View):
    def get(self,request):
        return render(request,'second.html',context={})

from myapp.models import Movie
class Movie_list(View):
    def get(self,request):
        m=Movie.objects.all()
        print(m)
        context={'movie':m}
        return render(request,'movielist.html',context)

class Add_movie(View):
    def get(self,request):
        return render(request,'addmovie.html')

    def post(self,request):
        print("hello")
        return render(request,'addmovie.html')