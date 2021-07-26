from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, request
from geoip2.models import ISP
from .models import details
from .forms import addnewrequirement
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.gis.geoip2 import GeoIP2
import geoip2.database
from geopy import distance

# Create your views here.
def ip_address(request):
    x_forwaded_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwaded_ip:
        ip = x_forwaded_ip.split(",")[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def home(request):
    return render(request, "main/home.html", {})


def display(request):
    dt = details.objects.all()
    ip = ip_address(request)
    reader = geoip2.database.Reader('./GeoLite2-City.mmdb')
    res = reader.city(ip)
    lati=res.location.latitude
    longi=res.location.longitude
    t=(lati,longi)
    loc_dict={}
    for i in dt:
        (lat_req,long_req)=(i.lat,i.long)
        loc_req=(lat_req,long_req)
        if distance.distance(t,loc_req).km<5:    
            loc_dict[i.id]=distance.distance(t,loc_req).km
    print(loc_dict)
    return render(request, "main/display.html", {"dt": dt,"loc_dict":loc_dict,})

def myposts(response):
    dt = details.objects.all()
    return render(response, "main/myposts.html", {"dt": dt})

def create(request):
    form = addnewrequirement(request.POST)
    if request.method == "POST":
        if form.is_valid():
            n = form.cleaned_data["name"]
            g = form.cleaned_data["gender"]
            b = form.cleaned_data["blood_type"]
            m = form.cleaned_data["mobile"]
            h = form.cleaned_data["hospital"]
            a = form.cleaned_data["address"]
            ip=ip_address(request)
            reader = geoip2.database.Reader('./GeoLite2-City.mmdb')
            res = reader.city(ip)
            la=res.location.latitude
            lon=res.location.longitude
            d1 = details(lat=la,long=lon,name=n, gender=g, blood_type=b,
                         mobile=m, hospital=h, address=a)
            d1.user=request.user
            d1.save()
    else:
        form = addnewrequirement()
    return render(request, "main/create.html", {"form": form})
