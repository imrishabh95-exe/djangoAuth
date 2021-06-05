from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate

# Create your views here.
#USER shasha - Rishabh95

def index(request):
    if request.user.is_anonymous:
        print(" +++++++++++++++++++++++++++++++  {}  ".format(request.user))
        return redirect('/login')
        #return render(request, 'login.html')
    return render(request, 'index.html')

def loginUser(request):
    print("-------------------------------------")
    if request.method == "POST":
        #check if user has entered correct credentials
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        print("YESSSSSSSSSSSSSSSSSSSSSSS  {} ------------------ {}".format(user_name,password))
        user = authenticate(request, username=user_name, password=password)
        print(" +++++++++++++++++++++++++++++++  {}  ".format(user))
        if user is not None:
            print("YESSSSSSSSSSSSSSSSSSSSSSS")
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
            print("Sorry wrong Password")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')
