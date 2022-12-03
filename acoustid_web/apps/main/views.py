from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")


def contact(request: HttpRequest) -> HttpResponse:
    return render(request, "contact.html")


def stats(request: HttpRequest) -> HttpResponse:
    return render(request, "stats.html")


def docs(request: HttpRequest) -> HttpResponse:
    return render(request, "docs.html")


def login(request: HttpRequest) -> HttpResponse:
    return render(request, "login.html")
