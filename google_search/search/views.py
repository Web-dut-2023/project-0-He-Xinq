from django.shortcuts import render, redirect


def index(request):
    return render(request, "search/index.html")


def images_search(request):
    return render(request, "search/images_search.html")


def advanced_search(request):
    return render(request, "search/advanced_search.html")


# Create your views here.
