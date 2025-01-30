from django.shortcuts import render,HttpResponse


def index(request):
    return render(request,'index.html')

def About(request):
    return render(request,'About.html')
   
def Home(request):
    return render(request,'Home.html')