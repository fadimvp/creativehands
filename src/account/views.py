from django.shortcuts import render

# Create your views here.


def register(request):

    context = {


    }

    return render(request,'register.html', context)


def Login (request):

    context ={

    }
    return render(request,'login.html',context)


def Logout(request):


    context= {

    }
    return render(request,'logout.html')