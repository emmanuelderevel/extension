from django.shortcuts import render, redirect
import requests
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'city/index.html', locals())

