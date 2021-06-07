from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("Placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/')

def show(request, num):
    return HttpResponse(f"Placeholder to display blog number:{num}")

def edit(request, num):
    return HttpResponse(f"PLaceholder to edit blog: {num}")

def destroy(request, num):
    return redirect('/blogs')

def jason(request):
    context  = {
        "title": "My First Blog",
        "content": "Lorem, ipsum blah blah blah blahb lahb."
    }
    return JsonResponse({"reponse:", context})


def secondFunction(request):
    print('**********')
    return index(request)