from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())


def details(request):
    template = loader.get_template("shop-details.html")
    return HttpResponse(template.render())


def shopGrid(request):
    template = loader.get_template("shop-grid.html")
    return HttpResponse(template.render())
