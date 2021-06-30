from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import details
from .forms import addnewrequirement
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

# Create your views here.


def home(response):
    return render(response, "main/home.html", {})


def display(response):
    dt = details.objects.all()
    if User.is_authenticated:
        return render(response, "main/display.html", {"dt": dt})
    else:
        return redirect(response, "main/login.html")


def create(response):
    if response.method == "POST":
        form = addnewrequirement(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            g = form.cleaned_data["gender"]
            b = form.cleaned_data["blood_type"]
            m = form.cleaned_data["mobile"]
            h = form.cleaned_data["hospital"]
            a = form.cleaned_data["address"]
            d1 = details(name=n, gender=g, blood_type=b,
                         mobile=m, hospital=h, address=a)
            d1.save()
    else:
        form = addnewrequirement()
    return render(response, "main/create.html", {"form": form})
