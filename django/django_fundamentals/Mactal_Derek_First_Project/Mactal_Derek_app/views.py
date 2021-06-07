from django.shortcuts import render, HttpResponse

def index(request):
    print("****************")
    print(request.path_info)
    return HttpResponse("Testing")

def dingusgreet(request, num):
    kitties = [
        {"name": "Derek", "age": 21},
        {"name": "boram", "age": 20},
        {"name": "suzie", "age": 5},
    ]
    
    context = {
        "num": num,
        "kitties": kitties
        }
    return render(request, "index.html", context)