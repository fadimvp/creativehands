from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404

def login(request):


    if request.method =='POST':
        username = request.POST['username1']

        # password = request.POST['password']
        # user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     login(request, user)
        #     # Redirect to a success page.
        #     ...
        # else:
        #     # Return an 'invalid login' error message.


    return render(request,'login.html',{})