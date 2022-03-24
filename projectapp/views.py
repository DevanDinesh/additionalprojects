from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    name="kerala"
    return render(request,'home.html',{'obj':name})
def about(request):
    return HttpResponse("Am about")
def contact(request):
    return render(request,'contact.html')
def detail(request):
    return HttpResponse('This is Detail page')
def thanks(request):
    return render(request,'thanks.html')
def home(request):
    name = "kerala"
    return render(request,'index.html',{'obj':name})
def operations(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    add = x+y
    sub = x-y
    mul = x*y
    div= x//y
    return render(request,'operations.html',{'addition':add,'substraction':sub,'multiplication':mul,'division':div})
