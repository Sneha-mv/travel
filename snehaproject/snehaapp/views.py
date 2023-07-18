from django.http import HttpResponse
from django.shortcuts import render
from .models import Place,Team

# Create your views here.
def demo(request):
    return HttpResponse("<h1>hello sneha</h1>")
def hello(request):
    return render(request,"hello.html")
def home(request):
    return HttpResponse("<h1>Welcome To Home Page</h1>")
def about(request):
    return render(request,"about.html")
def contact(request):
    return HttpResponse("<h3>You can contact us anytime</h3>")
def detail(request):
    return render(request,"detail.html")
def thanks(request):
    return HttpResponse("<h1>Thanks for coming Sneha</h1>")

def first(request):
    return render(request,"first-page.html")

def addition(request):
   x=int(request.GET["num1"])
   y=int(request.GET["num2"])
   res1=x+y
   res2=x-y
   res3=x*y
   res4=x/y
   res5=x//y
   res6=x%y
   res7=x**y
   return render(request,"result.html",{'result':res1,'result2':res2,'result3':res3,'result4':res4,'result5':res5,'result6':res6,'result7':res7})

def staticweb(request):
    obj= Place.objects.all()
    obt=Team.objects.all()
    return render(request, "index.html",{'result':obj,'res':obt})




