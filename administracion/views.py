from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from online.models import *
from online.forms import *
from . import forms

def landing_page(request):
    return render(request, 'index.html')

def login_page(request):
    return render(request, 'login.html')
