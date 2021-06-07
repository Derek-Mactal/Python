from django.shortcuts import render, HttpResponse, redirect
import datetime
from time import gmtime, strftime
def root(request):
    return redirect("/time_display")

def whatTimeIsiT(request):
    showtime = {
        "time": strftime("%b-%d-%Y %H:%M:%S", gmtime())
    }
    print('****************************')
    print(showtime)
    return render(request,'index.html', showtime)