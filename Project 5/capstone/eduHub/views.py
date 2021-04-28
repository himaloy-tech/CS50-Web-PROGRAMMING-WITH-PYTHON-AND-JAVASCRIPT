from django.shortcuts import render, HttpResponseRedirect
from .models import Course, Contact, User
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request, "index.html", {
        "Course":Course.objects.all()
    })

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request, "Invalid Credentials")
            return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "login.html")

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        user.save()
        auth_login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "register.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        message = request.POST.get('message')
        email = request.POST.get('email')
        obj = Contact.objects.create(name=name, message=message, email=email, user=request.user)
        obj.save()
        messages.success(request, "Your Query has been Successfully Submitted")
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "contact.html")

def search(request):
    if request.method == "POST":
        query = request.POST.get('query')
        object1 = Course.objects.filter(desc__icontains=query)
        object2 = Course.objects.filter(title__icontains=query)
        object3 = Course.objects.filter(category__icontains=query)
        result = object1.union(object2, object3)
        return render(request, "search.html", {
            "results": result
        })

def profile(request, username):
    if request.user.username == username:
        user = User.objects.get(username=username)
        return render(request, "profile.html", {
            "courses":user.enrolled_courses.all()
        })
