from multiprocessing import context
from django.shortcuts import render
from django.template.defaultfilters import title


# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')

class View_book(View):
    def get(self,request):
        book=Book.objects.all()
        context={'books':book}
        return render(request,viewbook.html,context)

class AddBook(View):
    def get(self,request):
        return render(request,'addbook.html')

    def post(self,request):
        data=request.POST

        t=data['title']
        a=data['author']
        pr=data['price']
        l=data['language']
        pa=data['pages']

        b=Book.objects.create(title=t,author=a,price=pr,language=l,pages=pa)
